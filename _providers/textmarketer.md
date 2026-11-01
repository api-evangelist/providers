---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/textmarketer/plans/textmarketer-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/textmarketer-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/textmarketer/llms/textmarketer-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/textmarketer-llms.txt
- group: other
  href: https://artifacts.apis.io/textmarketer/hosts/textmarketer-hosts.yml
  title: ''
  type: Hosts
  url: hosts/textmarketer-hosts.yml
- group: other
  href: https://artifacts.apis.io/textmarketer/vendors/textmarketer-vendors.yml
  title: ''
  type: Vendors
  url: vendors/textmarketer-vendors.yml
- group: build
  href: https://artifacts.apis.io/textmarketer/packages/textmarketer-packages.yml
  title: ''
  type: SDKs
  url: packages/textmarketer-packages.yml
- group: build
  href: https://artifacts.apis.io/textmarketer/packages/textmarketer-packages.yml
  title: ''
  type: Packages
  url: packages/textmarketer-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.textmarketer.co.uk/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TextMarketer
- group: auth
  href: https://artifacts.apis.io/textmarketer/security/textmarketer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/textmarketer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.textmarketer.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.textmarketer.co.uk/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://www.textmarketer.co.uk/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://www.textmarketer.co.uk/sms-gateway-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.textmarketer.co.uk/sign-up/
- group: operate
  title: ''
  type: Support
  url: https://www.textmarketer.co.uk/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.textmarketer.co.uk/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.textmarketer.co.uk/bulk-sms-prices/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.textmarketer.co.uk/termsandconditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.textmarketer.co.uk/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://www.textmarketer.co.uk/sign-up/
- group: start
  title: ''
  type: SignUp
  url: https://www.textmarketer.co.uk/signup/
coverage:
  checked: '2026-10-27'
  detail: The developer portal provides HTML documentation but no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL contracts.
  evidence:
  - status: 200
    url: https://www.textmarketer.co.uk/developers/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Text Marketer provides business SMS marketing services in the UK, offering bulk SMS, web SMS, SMS surveys, incoming SMS, short codes, email‑to‑SMS, and API integration for businesses to engage customers via text messaging. Their platform includes a developer portal, pricing plans, and resources such as guides and webinars to help users implement SMS solutions efficiently.
image: https://www.textmarketer.co.uk/wp-content/uploads/Hero-Image-01.svg
layout: provider
modified: '2026-10-27'
name: Text Marketer
nav: Providers
network: true
overview: 'Text Marketer is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include SMS, Marketing, UK, Business, and Communications.


  Text Marketer''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 14 more developer resources.'
plans:
- name: Textmarketer Plans Pricing
  plan_count: 3
  slug: textmarketer-plans-pricing
random_paper: 16
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 48.2
    operational_transparency: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 11.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Textmarketer Domain Security
  slug: textmarketer-domain-security
  summary_line: TLSv1.3 · DMARC
slug: textmarketer
tags:
- SMS
- Marketing
- UK
- Business
- Communications
website: https://www.textmarketer.co.uk/
---
