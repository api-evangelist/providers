---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://www.averlon.ai/responsible-disclosure
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/averlon/refs/heads/main/well-known/averlon-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/averlon-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/averlon/refs/heads/main/well-known/averlon-averlon-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/averlon-averlon-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/averlon/refs/heads/main/well-known/averlon-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/averlon-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/averlon/refs/heads/main/hosts/averlon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/averlon-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/averlon/refs/heads/main/vendors/averlon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/averlon-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.averlon.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.averlon.ai/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.averlon.ai/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/averlon/refs/heads/main/security/averlon-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/averlon-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/averlon/refs/heads/main/security/averlon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/averlon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.averlon.ai
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: Averlon provides an agentic AI platform that accelerates vulnerability remediation by automating the detection, prioritization, and fixing of security flaws. Leveraging AI-driven insights, Averlon reduces the exposure window from months to minutes, helping enterprises quickly mitigate risks and improve their security posture. The platform offers comprehensive resources including blogs, whitepapers, and research to support security teams.
image: https://cdn.prod.website-files.com/6792baf776d006a3f013bec4/67d24d527c897421f98315fe_Averlon-OpenGraph-3D.png
layout: provider
modified: '2026-09-26'
name: Averlon
nav: Providers
network: true
overview: 'Averlon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Artificial Intelligence, Vulnerability Management, and Automation.


  Averlon''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Averlon Domain Security
  slug: averlon-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Averlon Vulnerability Disclosure
  slug: averlon-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: averlon
tags:
- Company
- Security
- Artificial Intelligence
- Vulnerability Management
- Automation
website: https://www.averlon.ai
---
