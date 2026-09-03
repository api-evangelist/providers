---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    auth_clarity: bearer
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
  score: 5.0
  scored_at: '2026-09-03'
api_count: 5
apis:
- description: Institution-operated Shibboleth SAML 2.0 identity provider on the university's own host, published as machine-readable metadata in the GakuNin (学術認証フェデレーション) aggregate. EntityDescriptor ID PI0136JP, e
  name: Nagoya University Shibboleth Identity Provider (GakuNin)
  slug: identity-federation
- description: Open, machine-traversable HTTPS data archive operated by the ERG Science Center at Nagoya University's Institute for Space-Earth Environmental Research (ISEE, formerly STEL). It serves the Arase (ERG)
  name: ERG Science Center data archive (ISEE, Nagoya University)
  slug: ergsc-data-archive
- description: OAI-PMH 2.0 metadata harvesting interface for the NAGOYA Repository, Nagoya University's institutional repository. Verified live 2026-09-01 — verb=Identify returns 200 text/xml with repositoryName "NA
  name: NAGOYA Repository OAI-PMH (NII WEKO3 / JAIRO Cloud tenant)
  slug: repo-oai
- description: Nagoya University is registered in the Research Organization Registry as ROR ID https://ror.org/04chrp450, status active, established 1871, names "Nagoya University" / "名古屋大学" / "Nagoya Daigaku", webs
  name: ROR registration — Nagoya University
  slug: ror-registration
- description: Nagoya University is a participating institution in GakuNin (学術認証フェデレーション), the Japanese national academic access management federation operated by the National Institute of Informatics, and states so
  name: GakuNin academic access management federation membership
  slug: gakunin-federation
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://en.nagoya-u.ac.jp/
- group: other
  title: ''
  type: ResearchRepository
  url: https://nagoya.repo.nii.ac.jp/
- group: other
  title: ''
  type: IdentityFederation
  url: https://icts.nagoya-u.ac.jp/ja/services/gakunin/
- group: other
  title: ''
  type: OpenData
  url: https://ergsc.isee.nagoya-u.ac.jp/data/ergsc/
- group: other
  title: ''
  type: ResearchComputing
  url: https://icts.nagoya-u.ac.jp/ja/sc/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.nagoya-u.ac.jp/about-nu/declaration/ai/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://icts.nagoya-u.ac.jp/en/services/
- group: auth
  title: ''
  type: Authentication
  url: https://icts.nagoya-u.ac.jp/en/services/nuid/
- group: operate
  title: ''
  type: Support
  url: https://en.nagoya-u.ac.jp/site/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://en.nagoya-u.ac.jp/site/privacy/
- group: company
  title: ''
  type: Blog
  url: https://en.nagoya-u.ac.jp/research/activities/news/index.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/nagoya-university/
- group: design
  title: ''
  type: Conformance
  url: conformance/nagoya-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nagoya-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nagoya-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nagoya-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nagoya-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/nagoya-context.jsonld
created: '2026-06-03'
description: 'Nagoya University (名古屋大学) is a national research university in Nagoya, Aichi, Japan, founded 1871, a member of Japan''s Designated National University group and, since 2020, part of the Tokai National Higher Education and Research System (THERS) alongside Gifu University. It runs no developer portal, publishes no OpenAPI and issues no API keys, and this profile does not pretend otherwise. What it does operate, on its own nagoya-u.ac.jp hosts, are two genuinely institution-run machine surfaces: a Shibboleth SAML 2.0 identity provider (https://shib.nagoya-u.ac.jp/idp/shibboleth) registered in GakuNin, Japan''s academic access management federation, since 2014; and the ERG Science Center at the Institute for Space-Earth Environmental Research, which serves the Arase (ERG) satellite and ground-based observation data archive as an open, machine-traversable HTTPS tree that the pySPEDAS and SPEDAS analysis clients read directly. Its institutional repository, NAGOYA Repository, is
  a TENANT deployment on the National Institute of Informatics'' WEKO3 / JAIRO Cloud platform: the content, the metadata and the library administrators are Nagoya''s, but the OAI-PMH endpoint and its contract are NII''s and are not credited here. The university is registered in ROR (04chrp450) but is a member of neither DataCite nor Crossref — Japanese repositories mint DOIs through JaLC. Student records, course registration, the NU Portal and campus IT all sit behind THERS/GakuNin authentication and are not publicly documented developer APIs. Several relevant surfaces, including the university''s own GakuNin service documentation, exist only in Japanese.'
finops:
- name: Nagoya Finops
  service_category: Education
  slug: nagoya-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nagoya.png
jsonld:
- class_count: 16
  name: Nagoya Context
  property_count: 6
  slug: nagoya-context
layout: provider
modified: '2026-09-01'
name: Nagoya University
nav: Providers
network: true
overview: 'Nagoya University publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Japan, and Designated National University.


  The Nagoya University catalog on APIs.io includes 1 JSON-LD context.


  Nagoya University''s developer surface includes documentation, authentication, support, engineering blog, and 15 more developer resources.'
plans:
- name: Nagoya Plans Pricing
  plan_count: 2
  slug: nagoya-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Nagoya Rate Limits
  slug: nagoya-rate-limits
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 9
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 14.3
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 36.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 53.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nagoya/refs/heads/main/screenshots/nagoya-2026-06-20T185937.png
security:
- kind: authentication
  name: Nagoya Authentication
  slug: nagoya-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Nagoya Domain Security
  slug: nagoya-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nagoya
tags:
- Education
- Higher Education
- University
- Japan
- Designated National University
- Research
- Research Repository
- Open Access
- OAI-PMH
- Identity Federation
- Shibboleth
- Research Data
- Research Computing
website: https://en.nagoya-u.ac.jp/
---
