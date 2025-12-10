import sys
import dns.resolver
import re
from typing import List

EMAIL_REGEX = re.compile(r"^[^@]+@([^@]+\.[^@]+)$")

def extract_domain(email: str) -> str | None:
    match = EMAIL_REGEX.search(email.strip())
    if match:
        return match.group(1).lower()
    return None

def check_mx(domain: str) -> str:
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        mx_records = [r.exchange.to_text().rstrip('.') for r in answers]
        if mx_records:
            return "домен валиден"
        else:
            return "MX-записи отсутствуют или некорректны"
    except dns.resolver.NXDOMAIN:
        return "домен отсутствует"
    except dns.resolver.NoAnswer:
        return "MX-записи отсутствуют или некорректны"
    except dns.resolver.NoNameservers:
        return "MX-записи отсутствуют или некорректны (нет DNS-серверов)"
    except dns.exception.DNSException as e:
        return f"ошибка DNS: {str(e)}"
    except Exception as e:
        return f"неизвестная ошибка: {str(e)}"

def main():
    if len(sys.argv) < 2:
        print("Использование:")
        print("    python check_mx.py emails.txt")
        print("    или")
        print("    python check_mx.py email1@example.com email2@test.org ...")
        sys.exit(1)

    emails = []

    # Если передан файл
    if len(sys.argv) == 2 and sys.argv[1].endswith(('.txt', '.csv')):
        filename = sys.argv[1]
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and '@' in line:
                        emails.append(line)
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")
            sys.exit(1)
    else:
                emails = sys.argv[1:]

    if not emails:
        print("Не найдено ни одного email-адреса.")
        sys.exit(1)

    print(f"Проверяю {len(emails)} адрес(ов)...\n")
    print(f"{'Email':<40} {'Статус'}")
    print("-" * 60)

    for email in emails:
        domain = extract_domain(email)
        if not domain:
            status = "неверный формат email"
        else:
            status = check_mx(domain)
        print(f"{email:<40} {status}")

if __name__ == "__main__":
    main()