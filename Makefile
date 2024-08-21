run:
	/media/john/HDD1/odoopayment/odoo17-venv/bin/python3 /media/john/HDD1/odoopayment/odoo/odoo-bin -c /etc/odoo17.conf -u lms
crun:
	/media/john/HDD1/odoopayment/odoo17-venv/bin/python3 /media/john/HDD1/odoopayment/odoo/odoo-bin -c /etc/odoo17.conf
systemctlr:
	systemctl restart odoo17.servic