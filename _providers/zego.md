---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.zego.com
  baseurl_source: declared
  description: Match external users to Zego customers.
  name: Zego Customer Integration API
  slug: zego-customer-integration-api
- baseURL: https://api.zego.com
  baseurl_source: declared
  description: Customer status, validation, registration and enrolment.
  name: Zego Customers API
  slug: zego-customers-api
- baseURL: https://api.zego.com
  baseurl_source: declared
  description: Supported public liability occupations.
  name: Zego Occupations API
  slug: zego-occupations-api
- baseURL: https://api.zego.com
  baseurl_source: declared
  description: Fixed-term public liability policies.
  name: Zego Policies API
  slug: zego-policies-api
- baseURL: https://api.zego.com
  baseurl_source: declared
  description: Start and end insurance cover periods (shifts) for customers.
  name: Zego Shifts API
  slug: zego-shifts-api
artifact_total: 15
asyncapis:
- description: ''
  name: Zego Webhooks
  slug: zego-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zego Partner Customer Integration API
  slug: open-zego-customer-integration-api
- collection_type: open
  name: Zego Partner Customer Integration Customers API
  slug: open-zego-customers-api
- collection_type: open
  name: Zego Partner Customer Integration Occupations API
  slug: open-zego-occupations-api
- collection_type: open
  name: Zego Partner Customer Integration Policies API
  slug: open-zego-policies-api
- collection_type: open
  name: Zego Partner Customer Integration Shifts API
  slug: open-zego-shifts-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/zego-enrol-public-liability.md
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/zego-mcp.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zego-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.zego.com/security/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zego-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zego.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.zego.com/
- group: company
  title: ''
  type: Blog
  url: https://www.zego.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.zego.com/help/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zego.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zego.com/privacy/
created: '2026-07-17'
description: Zego is an FCA-regulated UK insurtech providing flexible, technology-driven motor and public-liability insurance built for the gig economy. Its telematics app (Sense) rewards safe driving, and it covers food-delivery and courier riders, private-hire and taxi drivers, van drivers, fleets, and learner drivers with monthly or annual policies. Zego works with partners such as Uber, Deliveroo, Just Eat and Amazon Flex, has served around 750,000 drivers and sold over 94 million policies. Beyond consumer products, Zego operates a RESTful Partner API (developer.zego.com, base URL api.zego.com) that lets work providers activate and deactivate insurance cover per shift, register and validate customers, enrol customers on public liability, issue fixed-term policies, and match external users to Zego customers, with signed webhooks for sign-up integration.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zego.png
layout: provider
modified: '2026-07-21'
name: Zego
nav: Providers
network: true
overview: 'Zego publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Customer Integration API, Customers API, Occupations API, and 2 more. Tagged areas include Company, Insurance, Insurtech, Motor Insurance, and Gig Economy.


  The Zego catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zego''s developer surface includes documentation, engineering blog, support, and 8 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 20.8
    developer_ergonomics: 30.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 28.6
  provenance:
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 39.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zego/refs/heads/main/screenshots/zego-2026-09-02T171533.png
security:
- kind: authentication
  name: Zego Authentication
  slug: zego-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Zego Domain Security
  slug: zego-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zego Vulnerability Disclosure
  slug: zego-vulnerability-disclosure
  summary_line: disclosure policy published
slug: zego
tags:
- Company
- Insurance
- Insurtech
- Motor Insurance
- Gig Economy
- Telematics
- Fleet Insurance
- Public Liability
- Partner API
website: https://www.zego.com/
---
