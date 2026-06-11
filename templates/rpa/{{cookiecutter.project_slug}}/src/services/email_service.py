import logging
import smtplib
import os
from email.message import EmailMessage
from pathlib import Path

logger = logging.getLogger(__name__)

SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")


class EmailService:
    def send(
        self,
        to: str | list[str],
        subject: str,
        body: str,
        attachments: list[Path] | None = None,
    ) -> None:
        msg = EmailMessage()
        msg["From"] = SMTP_USER
        msg["To"] = ", ".join([to] if isinstance(to, str) else to)
        msg["Subject"] = subject
        msg.set_content(body)

        for path in attachments or []:
            msg.add_attachment(
                path.read_bytes(),
                maintype="application",
                subtype="octet-stream",
                filename=path.name,
            )

        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(SMTP_USER, SMTP_PASSWORD)
            smtp.send_message(msg)
        logger.info("E-mail enviado para %s", to)
