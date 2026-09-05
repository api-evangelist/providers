---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: true
  source:
  - live probes
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
    consent_identity: true
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
  score: 7.2
  scored_at: '2026-09-04'
api_count: 8
apis:
- description: Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH 2.0) endpoint for DepositOnce, TU Berlin's institutional repository for publications and research data, operated by the University Li
  name: DepositOnce OAI-PMH Interface
  slug: depositonce-oai
- description: DSpace 9.4 REST/HAL API for DepositOnce, exposing communities, collections, items, bitstreams, discovery, versioning, COAR Notify (ldnservices) and usage reports. Anonymous access is genuinely partial
  name: DepositOnce DSpace REST API
  slug: depositonce-rest
- description: 'The institution''s own Shibboleth Identity Provider, operated by the ZECM and registered in the DFN-AAI federation. Its SAML 2.0 metadata is public and machine-readable — 15,920 bytes of XML declaring '
  name: TU Berlin Shibboleth Identity Provider (SAML 2.0 Metadata)
  slug: shibboleth-idp
- description: 'Self-hosted GitLab Enterprise Edition for TU Berlin. Correcting the June 2026 profile, which recorded this API as fully gated: unauthenticated reads of public resources succeed — GET /api/v4/projects '
  name: TU Berlin GitLab API
  slug: gitlab
- description: TU Berlin runs its own Matrix homeserver for institutional messaging, with an Element web client at chat.tu-berlin.de and documentation at docs.chat.tu-berlin.de. The Client-Server API answers unauthe
  name: TU Berlin Matrix Homeserver (Client-Server API)
  slug: matrix
- description: 'ISIS is TU Berlin''s central learning-management system, a Moodle instance on a TU Berlin host. It acts as an LTI 1.3 platform: a public RS256 JWKS is served at /mod/lti/certs.php (200, application/jso'
  name: ISIS (Moodle) LTI 1.3 Platform
  slug: isis-lti
- description: 'tubCloud is TU Berlin''s self-hosted Nextcloud file service, operated by the ZECM on a TU Berlin host. Only the capability probe is public: /status.php returns 200 with Nextcloud 32.0.9 Enterprise. The'
  name: tubCloud (Nextcloud) API
  slug: tubcloud
- description: The University Library's discovery layer runs on Ex Libris Primo at tu-berlin.hosted.exlibrisgroup.com — an institution-specific tenant on a vendor platform, reached from the library pages at www.tu.b
  name: University Library Discovery (Ex Libris Primo)
  slug: library-primo
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://www.tu.berlin/en
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chat.tu-berlin.de/
- group: docs
  title: ''
  type: Documentation
  url: https://depositonce.tu-berlin.de/info/help
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TU-Berlin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tuub
- group: build
  title: ''
  type: SourceCode
  url: https://git.tu-berlin.de/explore/projects
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/tu-berlin/
- group: company
  title: ''
  type: Blog
  url: https://blogs.tu-berlin.de/
- group: operate
  title: ''
  type: Support
  url: https://www.tu.berlin/en/campusmanagement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tu.berlin/en/data-protection
- group: other
  title: ''
  type: IdentityFederation
  url: https://shibboleth.tu-berlin.de/idp/shibboleth
- group: other
  title: ''
  type: IdentityFederation
  url: https://www.tu.berlin/campusmanagement/angebot/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://depositonce.tu-berlin.de/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://tu-berlin.hosted.exlibrisgroup.com/primo-explore/search?tab=tub_all&vid=TUB
- group: learn
  title: ''
  type: CourseCatalog
  url: https://moseskonto.tu-berlin.de/moses/verzeichnis/index.html
- group: other
  title: ''
  type: ResearchComputing
  url: https://hpc.wiki.tu-berlin.de/
- group: other
  title: ''
  type: AIPolicy
  url: https://digit.zewk.wiki.tu-berlin.de/doku.php?id=ki:richtlinien
- group: build
  title: ''
  type: AITooling
  url: https://www.tu.berlin/en/wm/services/it-services-and-software/pilot-project-chatgpt-edu
- group: auth
  title: ''
  type: Authentication
  url: https://www.tu.berlin/campusmanagement/angebot/shibboleth
- group: auth
  title: ''
  type: Authentication
  url: authentication/tu-berlin-authentication.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tu.berlin/en/campusmanagement/about/legal-provisions
- group: operate
  title: ''
  type: StatusPage
  url: https://www.tu.berlin/campusmanagement/angebot/aktueller-dienste-status
- group: auth
  title: ''
  type: Security
  url: https://www.tu.berlin/en/campusmanagement/it-security
- group: other
  title: ''
  type: ContentSignal
  url: https://www.tu.berlin/robots.txt
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tu-berlin-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tu-berlin-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tu-berlin-gitlab-openid-configuration.json
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tu-berlin-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tu-berlin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tu-berlin-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tu-berlin-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Technische Universität Berlin (TU Berlin) is a public technical research university in Berlin, Germany, and a member of the Berlin University Alliance and the TU9 alliance of German institutes of technology. It operates no central developer portal, publishes no OpenAPI, AsyncAPI or apis.json of its own, and sells no API product — its programmable footprint is the set of standards-based endpoints its own IT units expose on its own hosts, running third-party software. Confirmed live and unauthenticated: the DepositOnce institutional repository (DSpace 9, OAI-PMH with 15 metadata formats, a REST/HAL API and an OpenSearch description, minting DataCite DOIs under prefix 10.14279); a Shibboleth SAML 2.0 Identity Provider whose federation metadata is public (entityID https://ephraim.tu-berlin.de/shibboleth, DFN-AAI); a self-hosted GitLab whose REST v4 lists 2,851 public projects without credentials and which is its own OAuth2/OIDC provider; a Matrix homeserver (Synapse) with the Client-Server
  API answering openly; and ISIS, the institutional Moodle, acting as an LTI 1.3 platform with a public keyset. Library discovery is an Ex Libris Primo tenant, not TU Berlin engineering. Nothing here is an institution-authored contract, and none is claimed.'
finops:
- name: Tu Berlin Finops
  service_category: Education
  slug: tu-berlin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tu-berlin.png
jsonld:
- class_count: 17
  name: Tu Berlin Context
  property_count: 3
  slug: tu-berlin-context
layout: provider
modified: '2026-08-30'
name: Technical University of Berlin
nav: Providers
network: true
overview: 'Technical University of Berlin publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Technical University, and Germany.


  The Technical University of Berlin catalog on APIs.io includes 1 JSON-LD context.


  Technical University of Berlin''s developer surface includes documentation, engineering blog, support, authentication, and 28 more developer resources.'
plans:
- name: Tu Berlin Plans Pricing
  plan_count: 2
  slug: tu-berlin-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Tu Berlin Rate Limits
  slug: tu-berlin-rate-limits
scopes:
- name: Tu Berlin Scopes
  scope_count: 26
  slug: tu-berlin-scopes
  summary_line: 26 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: developing
  composite: 43.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 67.0
    catalog_earned_first_party: 0.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 14.3
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 43.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 79.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tu-berlin/refs/heads/main/screenshots/tu-berlin-2026-06-20T195818.png
security:
- kind: authentication
  name: Tu Berlin Authentication
  slug: tu-berlin-authentication
  summary_line: 7 schemes
- kind: domain-security
  name: Tu Berlin Domain Security
  slug: tu-berlin-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tu-berlin
tags:
- University
- Higher Education
- Education
- Technical University
- Germany
- Berlin
- Research Data
- Open Access
- Repository
- Library
- Identity Federation
- Course Catalog
- Research Computing
website: https://www.tu.berlin/en
---
