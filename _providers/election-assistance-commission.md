---
access_model:
  confidence: high
  label: Free, no registration, anonymous access
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
  - https://www.eac.gov/jsonapi
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.7
  scored_at: '2026-09-10'
api_count: 2
apis:
- baseURL: https://www.eac.gov/jsonapi
  baseurl_source: declared
  description: A live, anonymous, read-only JSON:API 1.0 surface served by the EAC's own Drupal 10 web platform at https://www.eac.gov/jsonapi. The EAC does not document, advertise or link to it from any developer p
  name: EAC Content JSON:API
  slug: eac
- description: 'The EAC''s federal open-data inventory, served at https://www.eac.gov/data.json and declaring conformance to the Project Open Data / DCAT-US v1.1 schema in the document itself. Probed 2026-09-06: HTTP '
  name: EAC Open Data Catalog
  slug: data-catalog
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://www.eac.gov
- group: other
  title: ''
  type: ResearchAndData
  url: https://www.eac.gov/research-and-data
- group: docs
  title: ''
  type: Documentation
  url: https://www.eac.gov/research-and-data
- group: other
  title: ''
  type: Datasets
  url: https://www.eac.gov/research-and-data/studies-and-reports
- group: other
  title: ''
  type: Standards
  url: https://www.eac.gov/voting-equipment/voluntary-voting-system-guidelines
- group: other
  title: ''
  type: RSS
  url: https://www.eac.gov/rss.xml
- group: company
  title: ''
  type: Newsroom
  url: https://www.eac.gov/news
- group: company
  title: ''
  type: Blog
  url: https://www.eac.gov/blogs
- group: operate
  title: ''
  type: Contact
  url: https://www.eac.gov/contact
- group: operate
  title: ''
  type: Support
  url: https://www.eac.gov/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eacgov
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eac.gov/main/privacy-statement
- group: other
  title: ''
  type: Accessibility
  url: https://www.eac.gov/accessibility-statement
- group: other
  title: ''
  type: FOIA
  url: https://www.eac.gov/foia/freedom-information-act-foia
- group: auth
  title: ''
  type: Security
  url: https://www.eac.gov/vulnerability-disclosure-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/election-assistance-commission-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/election-assistance-commission-domain-security.yml
- group: agent
  title: ''
  type: X-WellKnownProbe
  url: well-known/election-assistance-commission-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/election-assistance-commission-packages.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/u-s-election-assistance-commission
created: '2024-12-03'
description: 'The U.S. Election Assistance Commission (EAC) is an independent, bipartisan federal commission established by the Help America Vote Act of 2002 (HAVA). It adopts the Voluntary Voting System Guidelines, accredits voting system test laboratories, certifies voting systems, administers and audits HAVA grant funds, and is the national clearinghouse for election administration information. The EAC publishes no developer portal, no API documentation and no API key programme, but serves two real anonymous machine surfaces it does not advertise: a live read-only JSON:API 1.0 at https://www.eac.gov/jsonapi (Drupal 10, 216 resource types) carrying the certified voting system register, accredited test labs, manufacturers, Engineering Change Orders, Notices of Clarification, NVRA state pages, per-state registration deadlines, HAVA grant financials and 561 Clearinghouse Awards; and a Project Open Data v1.1 catalog at https://www.eac.gov/data.json listing the EAVS bulk datasets. Both verified.'
examples:
- key_count: 3
  name: Election Assistance Commission Eco Collection Example
  slug: election-assistance-commission-eco-collection-example
- key_count: 2
  name: Election Assistance Commission Error 400 Example
  slug: election-assistance-commission-error-400-example
- key_count: 2
  name: Election Assistance Commission Error 405 Readonly Example
  slug: election-assistance-commission-error-405-readonly-example
- key_count: 3
  name: Election Assistance Commission Jsonapi Index Example
  slug: election-assistance-commission-jsonapi-index-example
- key_count: 3
  name: Election Assistance Commission State Voter Info Example
  slug: election-assistance-commission-state-voter-info-example
- key_count: 4
  name: Election Assistance Commission Test Lab Sparse Fieldset Example
  slug: election-assistance-commission-test-lab-sparse-fieldset-example
- key_count: 4
  name: Election Assistance Commission Voting System Collection Example
  slug: election-assistance-commission-voting-system-collection-example
finops:
- name: Election Assistance Commission Finops
  service_category: API
  slug: election-assistance-commission-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/election-assistance-commission.png
layout: provider
modified: '2026-09-06'
name: Election Assistance Commission
nav: Providers
network: true
overview: 'Election Assistance Commission publishes 1 API on the [APIs.io](https://apis.io/) network: EAC Content JSON:API. Tagged areas include Federal-Government, Elections, Voting, Open Data, and Voting-Systems.


  Election Assistance Commission''s developer surface includes documentation, engineering blog, support, and 17 more developer resources.'
plans:
- name: Election Assistance Commission Plans Pricing
  plan_count: 0
  slug: election-assistance-commission-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Election Assistance Commission Rate Limits
  slug: election-assistance-commission-rate-limits
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 45.0
    catalog_earned_first_party: 5.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 33.3
    contract_quality: 57.8
    developer_ergonomics: 30.4
    discoverability: 68.5
    governance: 33.3
    operational_transparency: 15.8
  previous_composite: 41.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 50.0
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/election-assistance-commission/refs/heads/main/screenshots/election-assistance-commission-2026-06-20T180552.png
security:
- kind: authentication
  name: Election Assistance Commission Authentication
  slug: election-assistance-commission-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Election Assistance Commission Domain Security
  slug: election-assistance-commission-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Election Assistance Commission Vulnerability Disclosure
  slug: election-assistance-commission-vulnerability-disclosure
  summary_line: disclosure policy published
slug: election-assistance-commission
tags:
- Federal-Government
- Elections
- Voting
- Open Data
- Voting-Systems
- Certification
- Government-Data
- JSON-API
- Public-Records
website: https://www.eac.gov
---
