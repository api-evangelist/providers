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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://techcommunity.microsoft.com/tag/security
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/en-us
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/changelog
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/category/windows/blog/windows-itpro-blog
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/adaptive-cards/sdk/rendering-cards/android/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.microsoft.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: agent
  href: https://artifacts.apis.io/riskiq/llms/riskiq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/riskiq-llms.txt
- group: auth
  href: https://artifacts.apis.io/riskiq/well-known/riskiq-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/riskiq-security.txt
- group: agent
  href: https://artifacts.apis.io/riskiq/well-known/riskiq-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/riskiq-well-known.yml
- group: other
  href: https://artifacts.apis.io/riskiq/hosts/riskiq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/riskiq-hosts.yml
- group: other
  href: https://artifacts.apis.io/riskiq/vendors/riskiq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/riskiq-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.microsoft.com/privacy?icid=DSM_Footer_Company_Privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/security/pricing-overview
- group: auth
  href: https://artifacts.apis.io/riskiq/security/riskiq-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/riskiq-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/riskiq/security/riskiq-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/riskiq-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/riskiq/security/riskiq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/riskiq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/security/business/siem-and-xdr/microsoft-defender-threat-intelligence
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/riskiq
coverage:
  checked: '2026-11-05'
  detail: www.riskiq.com 301-redirects to the Microsoft Defender Threat Intelligence page and the former API hosts api.riskiq.net, api.passivetotal.org and community.riskiq.com refuse connections; only two frozen PyPI clients remain.
  evidence:
  - status: 301
    url: https://www.riskiq.com/
  - status: 0
    url: https://api.riskiq.net/
  - status: 0
    url: https://api.passivetotal.org/
  - status: 0
    url: https://community.riskiq.com/
  reason: defunct
  state: none
created: '2026-07-17'
description: RiskIQ was a San Francisco-based external threat intelligence and attack surface management company, known for its PassiveTotal platform (passive DNS, WHOIS, SSL certificate and host-pair intelligence), Digital Footprint external asset discovery, and External Threats brand/phishing detection. It exposed a developer REST API at api.riskiq.net and a research console at community.riskiq.com. Microsoft acquired RiskIQ in 2021 and folded its technology into Microsoft Defender Threat Intelligence (MDTI) and Microsoft Defender External Attack Surface Management (Defender EASM). As of this enrichment pass the riskiq.com domain runs on Microsoft/Azure infrastructure and www.riskiq.com issues a 301 redirect to the Microsoft Defender Threat Intelligence product page; the standalone RiskIQ/PassiveTotal API hosts (api.riskiq.net, community.riskiq.com) no longer accept connections. This profile is retained as a historical/acquired-company record with no live, independent API surface to enrich.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/riskiq.png
layout: provider
modified: '2026-11-05'
name: RiskIQ
nav: Providers
network: true
overview: 'RiskIQ is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Threat Intelligence, Attack Surface Management, and Cybersecurity.


  RiskIQ''s developer surface includes changelog, engineering blog, getting-started guide, documentation, support, pricing, and 16 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 25.0
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 57.1
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/riskiq/riskiq-2026-09-02T153856.png
security:
- kind: domain-security
  name: Riskiq Domain Security
  slug: riskiq-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Riskiq Vulnerability Disclosure
  slug: riskiq-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Riskiq Trust Center
  slug: riskiq-trust-center
  summary_line: GDPR
slug: riskiq
tags:
- Company
- Security
- Threat Intelligence
- Attack Surface Management
- Cybersecurity
- Passive DNS
- Acquired
website: https://www.microsoft.com/security/business/siem-and-xdr/microsoft-defender-threat-intelligence
---
