app_name = "apex_sign"
app_title = "ApexSign"
app_publisher = "GoldenJustin"
app_description = "Premier Enterprise Electronic Signature Solution"
app_email = "justin@example.com"
app_license = "MIT"

doc_events = {
	"ApexSign Document": {
		"before_insert": "apex_sign.api.validate_creation"
	}
}

website_route_rules = [
	{"from_route": "/sign/<name>", "to_route": "sign"},
]
