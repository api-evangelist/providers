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
  href: https://artifacts.apis.io/dtexsystems/security/dtexsystems-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dtexsystems-trust-center.yml
- group: other
  href: https://artifacts.apis.io/dtexsystems/hosts/dtexsystems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dtexsystems-hosts.yml
- group: build
  href: https://artifacts.apis.io/dtexsystems/integrations/dtexsystems-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/dtexsystems-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/dtexsystems/vendors/dtexsystems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dtexsystems-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.dtex.ai/newsroom/
- group: other
  title: ''
  type: Leadership
  url: https://www.dtex.ai/leadership/tam-vu/
- group: company
  title: ''
  type: Website
  url: https://www.dtex.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.dtex.ai/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://www.dtex.ai/resources/guides/
- group: operate
  title: ''
  type: Support
  url: https://support.mydtex.net/
- group: start
  title: ''
  type: SignUp
  url: https://www.dtex.ai/request-a-demo/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dtex.ai/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dtex.ai/terms-of-use/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.dtex.ai/
- group: auth
  href: https://artifacts.apis.io/dtexsystems/security/dtexsystems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dtexsystems-domain-security.yml
coverage:
  checked: '2026-10-20'
  detail: DTEX publishes no public API reference or spec; product documentation lives on the customer support portal support.mydtex.net, whose /mcp endpoint answers 403, and www.dtex.ai/llms.txt is 404.
  evidence:
  - status: 403
    url: https://support.mydtex.net/mcp
  - status: 404
    url: https://www.dtex.ai/llms.txt
  - status: 200
    url: https://support.mydtex.net/
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: DTEX Systems (DTEX) is a cybersecurity company delivering a risk-adaptive insider risk management platform. Its DTEX InTERCEPT product and Platform v7 unify insider threat detection, data loss prevention (DLP), user activity monitoring (UAM), and AI/agentic risk governance through behavioral intelligence rather than intrusive content inspection. The platform correlates human behavior across endpoints to surface early-warning indicators along the insider threat kill chain, uses OCSF-aligned connectors and standardized schemas to export enriched telemetry to SIEM, SOAR, and ITSM tooling, and ships agentic defenders (Triage Guardian and Threat Hunter) to automate investigations. DTEX is backed by Norwest Venture Partners and serves enterprise and government customers. It was surfaced as a portfolio company and enriched into the API Evangelist network; no public developer program, OpenAPI, or self-serve API documentation is currently published — integration is via the enterprise
  platform and OCSF connectors.
image: https://www.dtex.ai/wp-content/uploads/2024/08/DTEX-Main-Logo_Black.png
layout: provider
modified: '2026-10-20'
name: Dtexsystems
nav: Providers
network: true
overview: 'Dtexsystems is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Insider Risk Management, Data Loss Prevention, and User Activity Monitoring.


  Dtexsystems'' developer surface includes engineering blog, documentation, support, signup flow, and 11 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    operational_transparency: 0.0
  previous_composite: 17.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/dtexsystems/dtexsystems-2026-07-25T212438.png
security:
- kind: domain-security
  name: Dtexsystems Domain Security
  slug: dtexsystems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Dtexsystems Trust Center
  slug: dtexsystems-trust-center
  summary_line: trust center published
slug: dtexsystems
tags:
- Company
- Cybersecurity
- Insider Risk Management
- Data Loss Prevention
- User Activity Monitoring
- Behavioral Analytics
- AI Risk Governance
- Security
- Artificial Intelligence
- Risk Management
- Data Protection
website: https://www.dtex.ai/
---
