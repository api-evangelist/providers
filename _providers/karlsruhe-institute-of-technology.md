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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-09-01'
api_count: 9
apis:
- description: KITopen is KIT's central open-access institutional repository for the bibliographic data, full texts, images, research data and AV media of KIT scientists. It is built on dbkit, the web application fr
  name: KITopen OAI-PMH Interface
  slug: kitopen-oai
- description: 'The KIT Library self-hosts Koha, the open-source integrated library system, at katalog.bibliothek.kit.edu, and its REST API is live and served from KIT''s own registrable domain. Verified 2026-09-01: /'
  name: KIT Library Catalogue REST API (self-hosted Koha)
  slug: library-catalog-api
- description: 'RADAR4KIT is KIT''s interdisciplinary research-data repository for archiving and publishing research data with DOI assignment. It is a tenancy on the RADAR service operated by FIZ Karlsruhe, served on '
  name: RADAR4KIT Research Data Repository (RADAR tenancy)
  slug: radar4kit
- description: 'The Scientific Computing Center operates KIT''s Shibboleth SAML 2.0 Identity Provider and publishes its metadata as application/xml from KIT''s own host. Verified 2026-09-01: entityID https://idp.scc.ki'
  name: DFN-AAI Identity Federation — KIT Shibboleth Identity Provider
  slug: shibboleth-idp
- description: 'Separately from the Shibboleth IdP, the Scientific Computing Center operates a Keycloak OpenID Connect provider for the "kit" realm on KIT''s own domain. Verified 2026-09-01: the discovery document at '
  name: KIT OpenID Connect Provider (SCC Keycloak realm)
  slug: scc-oidc
- description: The Scientific Computing Center operates the KI-Toolbox, KIT's generative-AI service for staff, students and guest accounts, on KIT's own host. It fronts large language models hosted locally at the SC
  name: KI-Toolbox — KIT Generative AI Service (Open WebUI)
  slug: ki-toolbox
- description: 'KIT is a DataCite direct member, registering DOIs for its own research output rather than through a consortium proxy. Verified 2026-09-01 at https://api.datacite.org/providers/kit (200): id "kit", sym'
  name: DataCite Membership — Karlsruhe Institute of Technology (KIT)
  slug: datacite-member
- description: 'The KIT Library is a Crossref member in its own right, depositing DOIs under the prefix 10.58895. Verified 2026-09-01 at https://api.crossref.org/members/37766 (200): primary-name "Karlsruhe Institute'
  name: Crossref Membership — KIT Library
  slug: crossref-member
- description: KIT's Research Organization Registry identifier, https://ror.org/04t3en479, verified live 2026-09-01 against https://api.ror.org/organizations/04t3en479 (200). The record carries the website https://w
  name: ROR Registry Record — Karlsruhe Institute of Technology
  slug: ror-record
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://www.kit.edu/english/
- group: other
  title: ''
  type: ResearchRepository
  url: https://publikationen.bibliothek.kit.edu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://radar.kit.edu/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://katalog.bibliothek.kit.edu/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://campus.studium.kit.edu/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.scc.kit.edu/idp/shibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.nhr.kit.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.kit.edu/downloads/KI-Leitlinien-de.pdf
- group: build
  title: ''
  type: AITooling
  url: https://www.scc.kit.edu/en/services/ki-toolbox.php
- group: design
  title: ''
  type: Conformance
  url: conformance/karlsruhe-institute-of-technology-conformance.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/KIT-SCC
- group: build
  title: ''
  type: GitHub
  url: https://github.com/kit-data-manager
- group: build
  title: ''
  type: SourceCode
  url: https://gitlab.kit.edu/
- group: operate
  title: ''
  type: Support
  url: https://www.scc.kit.edu/en/services/servicedesk.php
- group: operate
  title: ''
  type: Support
  url: https://www.bibliothek.kit.edu/english/contact.php
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.kit.edu/.well-known/security.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kit.edu/legals.php
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kit.edu/privacypolicy.php
- group: company
  title: ''
  type: Blog
  url: https://www.kit.edu/kit/english/press_releases.php
- group: company
  title: ''
  type: BlogRSS
  url: https://www.kit.edu/english/news.rss
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/kit/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/karlsruhe-institute-of-technology-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/karlsruhe-institute-of-technology-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/karlsruhe-institute-of-technology-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/karlsruhe-institute-of-technology-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/karlsruhe-institute-of-technology-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Karlsruhe Institute of Technology (KIT) is a public research university and national research center of the Helmholtz Association in Karlsruhe, Germany, and a member of the TU9 alliance of German institutes of technology. KIT publishes no central developer portal and no institution-authored API contract: api.kit.edu, developer.kit.edu, data.kit.edu and opendata.kit.edu do not resolve at all. What it does operate, and what this profile records, is a set of standards-protocol and self-hosted surfaces on its own kit.edu domain, every one of them probed live on 2026-09-01 rather than taken from a link. The KIT Library runs an OAI-PMH 2.0 provider for the KITopen institutional repository (repositoryName "KITopen", built on the Library''s own dbkit framework) and a self-hosted Koha catalogue whose REST API answers keyless on its /public path. The Scientific Computing Center runs a Shibboleth SAML 2.0 Identity Provider registered in the DFN-AAI federation, a Keycloak OpenID Connect
  realm, and the KI-Toolbox, an Open WebUI deployment serving locally hosted large language models. RADAR4KIT, KIT''s research-data repository, is a tenancy on FIZ Karlsruhe''s RADAR service running on KIT infrastructure. KIT is a DataCite direct member and a Crossref member in its own right. Three of these surfaces answer with a product''s generic contract (Koha, RADAR, Open WebUI) rather than KIT''s own engineering; the deployments are recorded here and those contracts are deliberately not saved under KIT''s name.'
finops:
- name: Karlsruhe Institute Of Technology Finops
  service_category: Education
  slug: karlsruhe-institute-of-technology-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/karlsruhe-institute-of-technology.png
jsonld:
- class_count: 19
  name: Karlsruhe Institute Of Technology Context
  property_count: 0
  slug: karlsruhe-institute-of-technology-context
layout: provider
modified: '2026-09-01'
name: Karlsruhe Institute of Technology
nav: Providers
network: true
overview: 'Karlsruhe Institute of Technology publishes 1 API on the [APIs.io](https://apis.io/) network: KIT Library Catalogue REST API (self-hosted Koha). Tagged areas include Education, Higher Education, University, Technical University, and Germany.


  The Karlsruhe Institute of Technology catalog on APIs.io includes 1 JSON-LD context.


  Karlsruhe Institute of Technology''s developer surface includes GitHub presence, support, engineering blog, and 24 more developer resources.'
plans:
- name: Karlsruhe Institute Of Technology Plans Pricing
  plan_count: 2
  slug: karlsruhe-institute-of-technology-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Karlsruhe Institute Of Technology Rate Limits
  slug: karlsruhe-institute-of-technology-rate-limits
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 8
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 18.4
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 35.7
    discoverability: 85.2
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 24.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 57.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/karlsruhe-institute-of-technology/refs/heads/main/screenshots/karlsruhe-institute-of-technology-2026-06-20T183922.png
security:
- kind: domain-security
  name: Karlsruhe Institute Of Technology Domain Security
  slug: karlsruhe-institute-of-technology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Karlsruhe Institute Of Technology Vulnerability Disclosure
  slug: karlsruhe-institute-of-technology-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: karlsruhe-institute-of-technology
tags:
- Education
- Higher Education
- University
- Technical University
- Germany
- Europe
- Research
- Research Data
- Open Access
- Open Science
- Institutional Repository
- Library
- OAI-PMH
- Identity Federation
- Shibboleth
- Research Computing
- TU9
- Helmholtz Association
website: https://www.kit.edu/english/
---
