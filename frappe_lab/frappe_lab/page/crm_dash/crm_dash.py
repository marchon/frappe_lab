import frappe

@frappe.whitelist()
def get_crm_dash_data(from_date, to_date):
	data =  {
		"leads": [
			{"status":"Converted", "count":20, "percent":"50%"},
			{"status":"Lost", "count":12, "percent":"12%"},
			{"status":"Converted", "count":50, "percent":""},
		],
		"opportunities": [
			{"status":"Quotation", "count":35, "percent":"50%", "zfoo":"bar"},
			{"status":"Lost", "count":12, "percent":"12%", "zfoo":"bar"},
			{"status":"Converted", "count":50, "percent":"", "zfoo":"bar"},
			{"status":"Derezzed", "count":50, "percent":"", "zfoo":"bar"},
		]
	}

	html = "Problem"

	try:
		html = frappe.render_template("frappe_lab/frappe_lab/page/crm_dash/crm_dashboard.html", {"data": data})
	except Exception as e:
		for x in xrange(1,10):
			print ("FAILED", e)

	return html