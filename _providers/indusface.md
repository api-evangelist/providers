---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.indusface.com/security-accreditations/
- group: agent
  href: https://artifacts.apis.io/indusface/llms/indusface-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/indusface-llms.txt
- group: other
  href: https://artifacts.apis.io/indusface/hosts/indusface-hosts.yml
  title: ''
  type: Hosts
  url: hosts/indusface-hosts.yml
- group: other
  href: https://artifacts.apis.io/indusface/vendors/indusface-vendors.yml
  title: ''
  type: Vendors
  url: vendors/indusface-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.indusface.com/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://support.indusface.com/portal/en/home
- group: start
  title: ''
  type: SignUp
  url: https://www.indusface.com/register/apptrana-waap-free-trial/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.indusface.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.indusface.com/news-events/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.indusface.com/leadership/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.indusface.com/en/article/release-notes
- group: company
  title: ''
  type: Blog
  url: https://www.indusface.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.indusface.com/en/article/onboarding-to-apptrana
- group: docs
  title: ''
  type: Documentation
  url: https://docs.indusface.com/
- group: auth
  href: https://artifacts.apis.io/indusface/security/indusface-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/indusface-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/indusface/security/indusface-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/indusface-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://indusface.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://indusface.com/
  reason: no-developer-program
  state: none
created: '2026-10-20'
description: Indusface provides web application security solutions, offering a cloud‑based Web Application Firewall (WAF), vulnerability scanning, and continuous security monitoring. Their platform helps organizations protect against OWASP Top 10 threats, detect malicious traffic, and ensure compliance with industry standards. Founded to simplify application security, Indusface serves enterprises across multiple sectors, delivering real‑time threat intelligence and automated remediation capabilities.
image: https://www.indusface.com/images/indusface-og-logo.png
layout: provider
modified: '2026-10-20'
name: Indusface
nav: Providers
network: true
overview: 'Indusface is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Web Application Firewall, Cloud, Artificial Intelligence, and Enterprise.


  Indusface''s developer surface includes support, signup flow, changelog, engineering blog, getting-started guide, documentation, and 11 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 14.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 24.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/indusface/indusface-2026-11-03T133743.png
security:
- kind: domain-security
  name: Indusface Domain Security
  slug: indusface-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: trust-center
  name: Indusface Trust Center
  slug: indusface-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: indusface
tags:
- Security
- Web Application Firewall
- Cloud
- Artificial Intelligence
- Enterprise
website: https://indusface.com/
---
