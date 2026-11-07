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
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/clouddentistry/llms/clouddentistry-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clouddentistry-llms.txt
- group: auth
  href: https://artifacts.apis.io/clouddentistry/well-known/clouddentistry-faq-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clouddentistry-faq-security.txt
- group: agent
  href: https://artifacts.apis.io/clouddentistry/well-known/clouddentistry-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clouddentistry-well-known.yml
- group: other
  href: https://artifacts.apis.io/clouddentistry/hosts/clouddentistry-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clouddentistry-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clouddentistry.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clouddentistry.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.clouddentistry.com/login
- group: company
  title: ''
  type: Blog
  url: https://blog.clouddentistry.com/
- group: auth
  href: https://artifacts.apis.io/clouddentistry/security/clouddentistry-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clouddentistry-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://go.clouddentistry.com/
coverage:
  checked: '2026-10-09'
  detail: The provider's website does not expose any developer documentation or API specifications.
  evidence:
  - status: 200
    url: https://go.clouddentistry.com/
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: Clouddentistry provides a cloud-based platform for dental professionals, offering services such as practice management, patient membership programs, staffing solutions, continuing education, and dental industry reporting. The platform connects dentists, offices, and DSO solutions, enabling streamlined operations, recruitment, and patient engagement through an integrated digital ecosystem.
image: https://go.clouddentistry.com/wp-content/uploads/elementor/thumbs/Who-We-Are-1-rdljg0mbiuxr4xyqwnb7xpkbc309kj3sij8pll4pcm.png
layout: provider
modified: '2026-10-09'
name: Clouddentistry
nav: Providers
network: true
overview: 'Clouddentistry is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Dental, Cloud, Software-as-a-Service, Healthcare, and Platform.


  Clouddentistry''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 55.4
    operational_transparency: 10.5
  previous_composite: 14.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/clouddentistry/clouddentistry-2026-11-03T124506.png
security:
- kind: domain-security
  name: Clouddentistry Domain Security
  slug: clouddentistry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clouddentistry
tags:
- Dental
- Cloud
- Software-as-a-Service
- Healthcare
- Platform
- Company
website: https://go.clouddentistry.com/
---
