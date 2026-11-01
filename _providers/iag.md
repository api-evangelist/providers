---
access_model:
  confidence: low
  gated: partner
  gated_source:
  - tag:Partner Gated
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
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: IAG runs an Apigee gateway with brand virtual hosts api.iag.com.au, api.cgu.com.au, api.nrma.com.au and api.wfi.com.au (plus the non-production test-api.iag.com.au). Each answers every path, including
  name: Insurance Australia Group API Gateway (private)
  slug: iag-api-gateway
artifact_total: 8
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hackerone.com/en/articles/8509950-response-program-setup
- group: design
  href: https://artifacts.apis.io/iag/rules/iag-rules.yml
  title: ''
  type: Spectral
  url: rules/iag-rules.yml
- group: design
  href: https://artifacts.apis.io/iag/json-ld/iag-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/iag-context.jsonld
- group: design
  href: https://artifacts.apis.io/iag/vocabulary/iag-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/iag-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/iag/data-model/iag-data-model.yml
  title: ''
  type: DataModel
  url: data-model/iag-data-model.yml
- group: auth
  href: https://artifacts.apis.io/iag/well-known/iag-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/iag-security.txt
- group: other
  href: https://artifacts.apis.io/iag/hosts/iag-hosts.yml
  title: ''
  type: Hosts
  url: hosts/iag-hosts.yml
- group: other
  href: https://artifacts.apis.io/iag/vendors/iag-vendors.yml
  title: ''
  type: Vendors
  url: vendors/iag-vendors.yml
- group: auth
  href: https://artifacts.apis.io/iag/security/iag-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iag-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/iag
- group: auth
  href: https://artifacts.apis.io/iag/security/iag-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/iag-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/iag/conformance/iag-conformance.yml
  title: ''
  type: Conformance
  url: conformance/iag-conformance.yml
- group: company
  title: ''
  type: Website
  url: https://www.iag.com.au/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/InsuranceAustraliaGroup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/iagcl
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/iag
- group: company
  title: ''
  type: Newsroom
  url: https://www.iag.com.au/newsroom
- group: start
  title: ''
  type: SupplierPortal
  url: https://www.iag.com.au/supplier-portal
- group: start
  title: ''
  type: PartnerPortal
  url: https://www.cgu.com.au/eai/help
- group: operate
  title: ''
  type: Contact
  url: https://www.iag.com.au/contact-us
- group: other
  title: ''
  type: CorporateGovernance
  url: https://www.iag.com.au/about-us/corporate-governance/codes-and-policies
- group: company
  title: ''
  type: Careers
  url: https://careers.iag.com.au/
created: '2026-07-25'
description: 'Insurance Australia Group (IAG, ASX: IAG) is the largest general insurance company in Australia and New Zealand, headquartered in Sydney and operating a portfolio of underwriting brands rather than a single consumer-facing label. In Australia it trades as NRMA Insurance, CGU, WFI, Swann Insurance and the digital-native ROLLiN''; in New Zealand as State, AMI, NZI and Lumley. Its lines of business are property and casualty — home and contents, motor, commercial, rural and farm, compulsory third party and specialty — split across a Direct Insurance Australia arm and an Intermediated Insurance Australia arm that sells through brokers and authorised representatives. IAG has no public, self-serve API surface. Probing every conventional developer hostname on iag.com.au, cgu.com.au and nrma.com.au found no developer portal and no published reference documentation; docs.iag.com.au exists but immediately redirects to a Microsoft Entra ID sign-in and is an internal wall, not a portal.
  What the probes did confirm is a real Apigee API gateway fronting three brand virtual hosts — api.iag.com.au, api.cgu.com.au and api.nrma.com.au — each returning an Apigee ApplicationNotFound fault at the root, meaning proxies exist but none is discoverable or documented to the public. A second round of probing added a fourth brand virtual host, api.wfi.com.au, and a publicly resolvable non-production Apigee organisation at test-api.iag.com.au. IAG has also deployed MuleSoft''s Anypoint API Experience Hub and is migrating roughly 600 APIs onto it, with a stated intent to make them agent aware — a substantial API estate that is entirely internal. Broker and partner integration in this market runs through human-facing trading portals — CGU''s PolicyPlace quote-and-bind platform, the Ebix Sunrise Exchange and the Steadfast Client Trading Platform — not through an open API programme. IAG does run a HackerOne vulnerability disclosure programme, and published an RFC 9116 security.txt across
  seven brand domains until it was withdrawn in mid-2025. Australia has the legal machinery for open insurance and no live obligation: the Consumer Data Right that opened banking and energy was flagged for general insurance and then paused, so nothing compels IAG to publish. This record is therefore an honest stub: a partner-gated carrier with a private gateway and zero public specifications.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
jsonld:
- class_count: 120
  name: Iag Context
  property_count: 148
  slug: iag-context
layout: provider
modified: '2026-10-20'
name: Insurance Australia Group
nav: Providers
network: true
overview: 'Insurance Australia Group is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Australia, New Zealand, Property and Casualty, and General Insurance.


  The Insurance Australia Group catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Insurance Australia Group''s developer surface includes getting-started guide and 21 more developer resources.'
plans:
- name: Iag Plans Pricing
  plan_count: 0
  slug: iag-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Iag Rate Limits
  slug: iag-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Insurance Australia Group API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: iag-rules
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 14.7
    developer_ergonomics: 11.9
    discoverability: 67.9
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    - new-zealand
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 17.3
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 14.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/iag/iag-2026-07-25T221946.png
security:
- kind: authentication
  name: Iag Authentication
  slug: iag-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Iag Domain Security
  slug: iag-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Iag Vulnerability Disclosure
  slug: iag-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: iag
tags:
- Insurance
- Australia
- New Zealand
- Property and Casualty
- General Insurance
- Carrier
- Underwriting
- Claims
website: https://www.iag.com.au/
---
