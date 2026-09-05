---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: REST API for managing Cox customer accounts, including service subscriptions, billing information, user profiles, and service feature configuration for broadband, cable TV, and phone services.
  name: Cox Account Management API
  slug: cox-account-management-api
- description: REST API providing network diagnostic tools for Cox broadband subscribers, enabling troubleshooting of connectivity issues, signal level monitoring, equipment status checks, and service health assessm
  name: Cox Network Diagnostics API
  slug: cox-network-diagnostics-api
- description: REST API for Cox Business customers to manage voice, internet, and cloud connectivity services, including configuration of business phone systems, bandwidth management, and cloud networking options.
  name: Cox Business Services API
  slug: cox-business-services-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cox-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cox.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.cox.com/business/support/home.html
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/CoxCommunications
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cox-communications-inc.
- group: company
  title: ''
  type: Blog
  url: https://newsroom.cox.com/home
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cox.com/business/pricing.html
- group: operate
  title: ''
  type: StatusPage
  url: https://statusgator.com/services/cox-communications
- group: other
  title: ''
  type: X
  url: https://x.com/CoxComm
- group: commercial
  title: ''
  type: Plans
  url: plans/cox-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cox-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cox-finops.yml
created: '2026-06-13'
description: Cox Communications is a leading American telecommunications provider offering broadband internet, cable TV, and phone services for residential and business customers. Cox provides REST APIs for account management, service configuration, network diagnostics, and customer portal integrations across its broadband, cable television, and voice service platforms.
finops:
- name: Cox Finops
  service_category: ''
  slug: cox-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cox.png
layout: provider
modified: '2026-06-13'
name: Cox Communications
nav: Providers
network: true
overview: 'Cox Communications publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, Broadband, Cable TV, Internet, and Phone.


  Cox Communications'' developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Cox Plans Pricing
  plan_count: 5
  slug: cox-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Cox Rate Limits
  slug: cox-rate-limits
score:
  band: emerging
  composite: 20.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 55.0
    catalog_earned_first_party: 0.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 20.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Cox Domain Security
  slug: cox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cox Vulnerability Disclosure
  slug: cox-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cox
tags:
- Telecommunications
- Broadband
- Cable TV
- Internet
- Phone
- Account Management
- Network Diagnostics
website: https://www.cox.com
---
