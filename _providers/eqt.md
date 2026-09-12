---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 13.7
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eqt-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eqt-corporation
- group: company
  title: ''
  type: Website
  url: https://www.eqt.com
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.eqt.com/investor-relations/overview/default.aspx
- group: other
  title: ''
  type: Sustainability
  url: https://www.eqt.com/sustainability
- group: start
  title: ''
  type: X-CustomerPortal
  url: https://customers.equitransmidstream.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/eqt-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/eqt-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eqt-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EQTCorporation
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eqt.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eqt.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.eqt.com/about/contact
- group: company
  title: ''
  type: Blog
  url: https://www.eqt.com/thought-leadership
- group: other
  title: ''
  type: X-InformationalPostings
  url: https://infopost.eqt.com/
coverage:
  checked: '2026-09-06'
  detail: EQT publishes no API at all, and the one public machine-relevant surface it is required to serve — the FERC Informational Postings Web Site for its Equitrans interstate pipelines at infopost.eqt.com — is a Salesforce Experience Cloud single-page app whose Capacity, Index Of Customers, Nominations and Tariff postings exist only after JavaScript runs, with CSV export generated in the browser and the deeper posting routes answering 401 to anonymous callers.
  evidence:
  - status: 200
    url: https://infopost.eqt.com/
  - status: 401
    url: https://customers.equitransmidstream.com/IPWS-Gathering/Informational%20Postings/Operationally%20Available.aspx
  - status: 404
    url: https://www.eqt.com/llms.txt
  - status: 200
    url: https://infopost.eqt.com/.well-known/openid-configuration
  reason: js-rendered-docs
  state: unreadable
created: '2024-07-02'
description: 'EQT Corporation is the largest producer of natural gas in the United States, headquartered in Pittsburgh, Pennsylvania. It is a vertically integrated Appalachian Basin operator: upstream exploration and production, plus the interstate gathering and transmission pipelines it acquired with Equitrans Midstream in July 2024. EQT pairs production technology with environmental stewardship commitments, including a Scope 1 and Scope 2 net-zero target it reports as met ahead of its 2025 goal. EQT runs no developer program and publishes no API. Its only machine-readable public documents are the OpenID Connect discovery metadata of two Salesforce customer portals — infopost.eqt.com, the FERC-mandated Informational Postings site for its interstate pipelines, and customers.equitransmidstream.com — whose posting data renders client-side and is otherwise gated to registered customers. Not the Swedish firm EQT AB.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eqt.png
layout: provider
modified: '2026-09-06'
name: EQT Corporation
nav: Providers
network: true
overview: 'EQT Corporation is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Natural Gas, Oil and Gas, Appalachian Basin, and Fortune 1000.


  EQT Corporation''s developer surface includes support, engineering blog, and 13 more developer resources.'
press:
- date: '2026-05-25'
  title: EQT And Context Labs Announce Strategic Partnership
  url: https://ir.eqt.com/investor-relations/news/news-release-details/2023/EQT-And-Context-Labs-Announce-Strategic-Partnership/default.aspx
- date: '2026-05-25'
  title: News Releases
  url: https://www.perficient.com/about/newsroom/news-releases
- date: '2026-05-25'
  title: EQT Group's Post
  url: https://www.linkedin.com/posts/eqt-group_today-were-proud-to-introduce-eqts-ai-activity-7452400818386980864-uf-h
- date: '2026-05-25'
  title: A Powerful Synergy of AI and Human Expertise
  url: https://eqtgroup.com/en/about/motherbrain
- date: '2026-05-25'
  title: EQT Introduces AI Infrastructure Strategy to Help Build ...
  url: https://www.prnewswire.com/news-releases/eqt-introduces-ai-infrastructure-strategy-to-help-build-the-foundation-of-the-ai-economy-302748973.html
random_paper: 15
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 13.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/eqt/refs/heads/main/screenshots/eqt-2026-06-20T180803.png
security:
- kind: authentication
  name: Eqt Authentication
  slug: eqt-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Eqt Domain Security
  slug: eqt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: eqt
tags:
- Energy
- Natural Gas
- Oil and Gas
- Appalachian Basin
- Fortune 1000
website: https://www.eqt.com
---
