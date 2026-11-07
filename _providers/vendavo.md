---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - rate-limits
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/vendavo/hosts/vendavo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vendavo-hosts.yml
- group: build
  href: https://artifacts.apis.io/vendavo/integrations/vendavo-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/vendavo-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/vendavo/vendors/vendavo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vendavo-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.vendavo.com/security/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vendavo.com/platform/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.vendavo.com/company/press/
- group: other
  title: ''
  type: Leadership
  url: https://www.vendavo.com/company/leadership/
- group: company
  title: ''
  type: Website
  url: http://www.vendavo.com/
- group: company
  title: ''
  type: Blog
  url: https://www.vendavo.com/insights/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.vendavo.com/company/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vendavo.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vendavo.com/privacy-policy/
- group: agent
  href: https://artifacts.apis.io/vendavo/llms/vendavo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vendavo-llms.txt
- group: auth
  href: https://artifacts.apis.io/vendavo/security/vendavo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vendavo-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vendavo
- group: auth
  href: https://artifacts.apis.io/vendavo/security/vendavo-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/vendavo-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/vendavo/security/vendavo-trust-center.yml
  title: ''
  type: Compliance
  url: security/vendavo-trust-center.yml
- group: design
  href: https://artifacts.apis.io/vendavo/conformance/vendavo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vendavo-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/vendavo/plans/vendavo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vendavo-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/vendavo/rate-limits/vendavo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/vendavo-rate-limits.yml
coverage:
  checked: '2026-10-20'
  detail: Vendavo's documentation portal one.vendavo.com still 301s to an Atlassian ID-gated Confluence space, api.vendavo.com does not resolve, and the only MCP-shaped path (info.vendavo.com/api/mcp) is a Marketo endpoint answering 401 Access Denied, so its marketed real-time APIs are documented only for tenants.
  evidence:
  - status: 301
    url: https://one.vendavo.com/
  - status: 401
    url: https://info.vendavo.com/api/mcp
  - status: 200
    url: https://www.vendavo.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: 'Vendavo is an enterprise B2B commercial-excellence software company whose platform helps manufacturers and distributors optimize pricing, automate quoting and agreements, and manage rebate and incentive programs using AI-powered pricing intelligence and margin analytics. Vendavo has been named a Leader in the Gartner Magic Quadrant for B2B Pricing & Rebate Optimization Software and integrates with enterprise ERP, CRM, and eCommerce systems. Vendavo markets "real-time APIs for dynamic pricing and quoting workflows" alongside batch and file-based integration, but as of this enrichment pass it publishes no public developer portal, API reference or machine-readable contract: the Vendavo Documentation Portal (one.vendavo.com) redirects to an Atlassian ID login and the support portal to a Salesforce Community login, so the integration surface is reachable only by contracted customers and partners. Vendavo does publish a substantive public security posture — ISO/IEC 27001:2022, annual
  SOC 1 and SOC 2 Type 2 audits, a CSA STAR CAIQ self-assessment and a Trust Center at trustvault.vendavo.com. This profile was seeded as a portfolio lead of DCM Ventures and Sapphire Ventures.'
image: https://www.vendavo.com/wp-content/uploads/2026/04/Image-2-1024x431.png
layout: provider
modified: '2026-10-20'
name: Vendavo
nav: Providers
network: true
overview: 'Vendavo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Pricing, CPQ, and Quoting.


  Vendavo''s developer surface includes pricing, engineering blog, support, and 17 more developer resources.'
plans:
- name: Vendavo Plans Pricing
  plan_count: 0
  slug: vendavo-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Vendavo Rate Limits
  slug: vendavo-rate-limits
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.9
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 21.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa-cpra
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/vendavo/vendavo-2026-09-02T165629.png
security:
- kind: domain-security
  name: Vendavo Domain Security
  slug: vendavo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Vendavo Trust Center
  slug: vendavo-trust-center
  summary_line: ISO/IEC 27001:2022, SOC 1 Type 2, SOC 2 Type 2, CSA STAR Level 1 (CAIQ self-assessment), ISO 22301
slug: vendavo
tags:
- Company
- Enterprise
- Pricing
- CPQ
- Quoting
- Rebates
- B2B
- Commercial Optimization
- Margin Optimization
- Artificial Intelligence
website: http://www.vendavo.com/
---
