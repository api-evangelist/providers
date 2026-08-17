---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.9
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/rr-donnelley-and-sons-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rr-donnelley-and-sons-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rr-donnelley-and-sons-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rr-donnelley
- group: company
  title: ''
  type: Website
  url: https://www.rrd.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.rrd.com/solutions/connectone
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.rrd.com/home/default.aspx
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/rr-donnelley-and-sons/refs/heads/main/vocabulary/rr-donnelley-and-sons-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/rr-donnelley-and-sons/refs/heads/main/json-ld/rr-donnelley-and-sons-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://www.rrd.com/about/newsroom
- group: auth
  title: ''
  type: Security
  url: security/rr-donnelley-and-sons-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: security/rr-donnelley-and-sons-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rr-donnelley-and-sons-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rr-donnelley-and-sons-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/rr-donnelley-and-sons-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rr-donnelley-and-sons-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/rr-donnelley-and-sons-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rr-donnelley-and-sons-rate-limits.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rrd.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rrd.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.rrd.com/contact-us
- group: start
  title: ''
  type: Login
  url: https://connectone.rrd.com/
coverage:
  checked: '2026-08-13'
  detail: RRD's own API help page (intl.rrd.com/Help, indexed publicly as "RR Donnelley API" and stating that customer-facing APIs require a Username and APIKey header) refuses TCP 443 from two independent networks, api.rrd.com resolves to 162.27.32.131 with ports 443 and 80 filtered, and the ConnectOne customer storefront answers 401 on every path — the API exists but only contracted customers can read a byte of it.
  evidence:
  - status: 0
    url: https://intl.rrd.com/Help
  - status: 401
    url: https://connectone.rrd.com/openapi.json
  - status: 404
    url: https://www.rrd.com/openapi.json
  - status: 200
    url: https://www.rrd.com/.well-known/security.txt
  reason: customer-only-docs
  state: gated
created: '2025-01-01'
description: 'RR Donnelley & Sons Company (RRD) is a global provider of integrated communications services, offering marketing, business communications, commercial printing, direct mail, print fulfillment, labels, logistics, print management, and digital communications. RRD''s ConnectOne platform provides end-to-end marketing communications management including web-to-print storefronts, workflow automation, content management, and multichannel campaign execution. RRD serves enterprises across financial services, healthcare, retail, and other industries. RRD operates customer-facing APIs — its own help page states they authenticate with a Username and APIKey request header — but they are reachable only by contracted customers: the API help host refuses public connections, api.rrd.com has its ports filtered, and the ConnectOne storefront returns 401 on every path. No machine-readable contract is published anonymously.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rr-donnelley-and-sons.png
json_schemas:
- name: RR Donnelley Print Order
  property_count: 15
  slug: rr-donnelley-and-sons-print-order
jsonld:
- class_count: 0
  name: Rr Donnelley And Sons Context
  property_count: 18
  slug: rr-donnelley-and-sons-context
layout: provider
modified: '2026-08-13'
name: RR Donnelley And Sons
nav: Providers
network: true
overview: 'RR Donnelley And Sons is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Communications, Marketing, Print Services, Direct Mail, and Logistics.


  The RR Donnelley And Sons catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RR Donnelley And Sons'' developer surface includes documentation, engineering blog, support, and 19 more developer resources.'
plans:
- name: Rr Donnelley And Sons Plans Pricing
  plan_count: 0
  slug: rr-donnelley-and-sons-plans-pricing
press:
- date: '2026-05-25'
  title: SEC Charges R.R. Donnelley & Sons Co. with ...
  url: https://www.sec.gov/newsroom/press-releases/2024-75
- date: '2026-05-25'
  title: Newsroom Images | Download RRD Press Photos
  url: https://www.rrd.com/about/newsroom/images
- date: '2026-05-25'
  title: Boosting Brand Impact and Influence via Artificial Intelligence
  url: https://www.rrd.com/resources/blog/boosting-brand-impact-and-influence-via-artificial-intelligence
- date: '2026-05-25'
  title: RRD's AI-Powered Business Communication Intelligence ...
  url: https://www.rrd.com/about/newsroom/press-release/rrds-ai-powered-business-communication-intelligence-platform-streamlines-and-improves-customer-communications
- date: '2026-05-25'
  title: 'RRD Survey: Marketers Embrace Technology to ...'
  url: https://www.businesswire.com/news/home/20240411726617/en/RRD-Survey-Marketers-Embrace-Technology-to-Strategically-Integrate-Print-and-Digital
random_paper: 5
rate_limits:
- limit_count: 0
  name: Rr Donnelley And Sons Rate Limits
  slug: rr-donnelley-and-sons-rate-limits
rules:
- name: RR Donnelley And Sons API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rr-donnelley-and-sons-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.1
  delta: 12.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 12.9
    developer_ergonomics: 15.2
    discoverability: 57.4
    governance: 81.3
    operational_transparency: 10.5
  previous_composite: 20.2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/rr-donnelley-and-sons/refs/heads/main/screenshots/rr-donnelley-and-sons-2026-06-20T193234.png
security:
- kind: domain-security
  name: Rr Donnelley And Sons Domain Security
  slug: rr-donnelley-and-sons-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rr Donnelley And Sons Vulnerability Disclosure
  slug: rr-donnelley-and-sons-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Rr Donnelley And Sons Trust Center
  slug: rr-donnelley-and-sons-trust-center
  summary_line: ISO/IEC 27001, SOC 1 Type 2, SOC 2 Type 2, SOC 2 + HITRUST, PCI DSS, ISO 22301:2019, Cyber Essentials Plus
slug: rr-donnelley-and-sons
tags:
- Communications
- Marketing
- Print Services
- Direct Mail
- Logistics
- Fortune 1000
website: https://www.rrd.com
---
