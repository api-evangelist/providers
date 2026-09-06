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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clickdiagnostics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mpower-social.com/
- group: company
  title: ''
  type: About
  url: https://mpower-social.com/about-us/
- group: other
  title: ''
  type: Team
  url: https://mpower-social.com/our-team/
- group: other
  title: ''
  type: Services
  url: https://mpower-social.com/services/
- group: other
  title: ''
  type: Impact
  url: https://mpower-social.com/impact/
- group: other
  title: ''
  type: Awards
  url: https://mpower-social.com/awards/
- group: company
  title: ''
  type: Careers
  url: https://mpower-social.com/career/
- group: operate
  title: ''
  type: Contact
  url: https://mpower-social.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://mpower-social.com/blog/
- group: company
  title: ''
  type: BlogFeeds
  url: https://mpower-social.com/feed/
- group: company
  title: ''
  type: News
  url: https://mpower-social.com/news-events/
- group: other
  title: ''
  type: BrandAssets
  url: https://mpower-social.com/brand-assets/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Mpower-social
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/Mpower-social
- group: other
  title: ''
  type: GooglePlay
  url: https://play.google.com/store/apps/developer?id=mPower+Social+Enterprises+Ltd
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mpower-social.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mpower-social.com/privacy-policy-2/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mpowersoc
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/mpowersoc
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/mPowerSocial
- group: company
  title: ''
  type: Investors
  url: https://forgeglobal.com/clickdiagnostics_stock/
- group: build
  title: ''
  type: Packages
  url: packages/clickdiagnostics-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clickdiagnostics-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/clickdiagnostics-conformance.yml
coverage:
  checked: '2026-08-09'
  detail: mPower Social is an ICT4D implementer that builds bespoke DHIS2, OpenMRS, OpenSRP/FHIR Core, Bahmni and Moodle systems inside client governments and NGOs, so the only APIs in its work belong to those upstream projects; mpower-social.com is a WordPress marketing site with no /developers or /api page, api./docs./developer. do not resolve in DNS, and the one technical subdomain that does resolve — dhis2.mpower-social.com — never answers on port 443 from the public internet.
  evidence:
  - status: 404
    url: https://mpower-social.com/openapi.json
  - status: 404
    url: https://mpower-social.com/api-docs
  - status: 404
    url: https://mpower-social.com/llms.txt
  - status: 404
    url: https://mpower-social.com/.well-known/agent-card.json
  - status: 404
    url: https://mpower-social.com/.well-known/security.txt
  - status: 0
    url: https://dhis2.mpower-social.com/api/system/info
  reason: no-developer-program
  state: none
created: '2026-08-09'
description: mPower Social Enterprises Ltd. is a Dhaka, Bangladesh technology-for-development company founded in 2008 by Harvard and MIT graduate students as ClickDiagnostics — winner of the MIT $100K competition — and renamed after moving its center of gravity to Bangladesh in 2010. mPower designs, builds and operates information systems for governments, UN agencies, donor organizations and international NGOs across health and nutrition, water and sanitation, agriculture and livestock, education, governance and rights, livelihood and poverty alleviation, climate and environment, and humanitarian response, and states it has deployed more than 300 ICT solutions across 17 countries in the Global South. Its engineering practice is built on open-source digital public goods — DHIS2, OpenMRS, OpenSRP / FHIR Core, Bahmni and Moodle — which it customizes, integrates and supports for national health management information systems, electronic medical records and shared health records, rather than
  shipping a hosted product of its own. The company is ISO 9001:2015 certified. mPower publishes no public API, developer portal, or machine-readable contract; its public software surface is a GitHub organization made up largely of downstream forks of the open-source health platforms it implements, plus a set of first-party Android apps on Google Play.
image: https://mpower-social.com/wp-content/uploads/2024/09/mPower-icon.png
layout: provider
modified: '2026-08-09'
name: mPower Social
nav: Providers
network: true
overview: 'mPower Social is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, ICT4D, International Development, Digital Health, and Health Information Systems.


  mPower Social''s developer surface includes engineering blog, product news, and 23 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 10.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clickdiagnostics/refs/heads/main/screenshots/clickdiagnostics-2026-09-02T145108.png
security:
- kind: domain-security
  name: Clickdiagnostics Domain Security
  slug: clickdiagnostics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: clickdiagnostics
tags:
- Company
- ICT4D
- International Development
- Digital Health
- Health Information Systems
- Global Health
- Open-Source
- DHIS2
- OpenMRS
- FHIR
- Agriculture
- Education
- Humanitarian
- Bangladesh
- Consulting
website: https://mpower-social.com/
---
