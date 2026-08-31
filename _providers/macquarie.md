---
access_model:
  confidence: high
  label: Free · No signup, no key
  onboarding: unknown
  pricing: free
  public: true
  source:
  - authentication
  - probes
  trial: false
  try_now: true
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: 'The one institution-operated, keyless, machine-readable API surface Macquarie publishes. OAI-PMH 2.0 metadata harvesting for the Macquarie University Research Portal, served from the university''s own '
  name: Macquarie University Research Portal OAI-PMH
  slug: research-portal-oai-pmh
- description: Macquarie operates its own Shibboleth identity provider at idp.mq.edu.au, publishing SAML 2.0 metadata anonymously at /idp/shibboleth and registered in the Australian Access Federation as entityID urn
  name: Macquarie University Identity Provider (Shibboleth / SAML 2.0)
  slug: idp-shibboleth
- description: Macquarie self-hosts its learning management system as iLearn at ilearn.mq.edu.au and the Moodle web services REST endpoint answers publicly with a structured invalidtoken error, so the service exists
  name: Macquarie University iLearn (Moodle) Web Services
  slug: ilearn-moodle-webservices
- description: The Macquarie University Library publishes six public repositories on GitHub as the mqlibrary organisation — an Alma toolkit (now archived), resource-sharing partner harvest and sync services, and sma
  name: Macquarie University Library Open-Source Tooling
  slug: library-alma-tools
- description: Macquarie's research-information system is Elsevier Pure, tenanted on Macquarie hosts — researchers.mq.edu.au for the public portal and research-management.mq.edu.au for the administrative side. The P
  name: Macquarie University Research Portal (Elsevier Pure)
  slug: research-portal-pure
- description: The Macquarie University Research Data Repository is Figshare for Institutions, tenanted at figshare.mq.edu.au with DOI prefix 10.25949 minted through DataCite as ARDCX.MQU. The data, the DOIs and the
  name: Macquarie University Research Data Repository (Figshare)
  slug: rdr-figshare
- description: The Macquarie course handbook runs on CourseLoop as tenant siteId mq-prod-pres, served at coursehandbook.mq.edu.au from a shared vendor API at api-ap-southeast-2.prod.courseloop.com. The curriculum da
  name: Macquarie University Course Handbook (CourseLoop)
  slug: course-handbook-courseloop
- description: Library discovery for Macquarie runs on Ex Libris Primo at multisearch.mq.edu.au. The holdings are Macquarie's; Primo and the Alma platform beneath it are Ex Libris's, and the Alma/Primo APIs are gate
  name: Macquarie University Library MultiSearch (Ex Libris Primo)
  slug: library-multisearch-primo
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://www.mq.edu.au/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mqlibrary
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/macquarie-university/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.mq.edu.au/idp/shibboleth
- group: other
  title: ''
  type: IdentityFederation
  url: https://md.aaf.edu.au/aaf-metadata.xml
- group: other
  title: ''
  type: ResearchRepository
  url: https://researchers.mq.edu.au/
- group: other
  title: ''
  type: ResearchRepository
  url: https://figshare.mq.edu.au/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://coursehandbook.mq.edu.au/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://multisearch.mq.edu.au/
- group: other
  title: ''
  type: AIPolicy
  url: https://policies.mq.edu.au/document/view.php?id=394
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.mq.edu.au/document/view.php?id=107
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.mq.edu.au/document/view.php?id=234
- group: docs
  title: ''
  type: Documentation
  url: https://libguides.mq.edu.au/research_data_repository
- group: operate
  title: ''
  type: Support
  url: https://policies.mq.edu.au/contact.php
- group: design
  title: ''
  type: Conformance
  url: conformance/macquarie-domain-standards.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/macquarie-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/macquarie-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/macquarie-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/macquarie-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/macquarie-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Macquarie University is a public research university in Sydney, Australia. Its programmable footprint is small, real, and almost entirely indirect: it operates no developer portal, no open-data platform, and no central API programme. The one institution-operated, keyless, machine-readable API surface found is the Macquarie University Research Portal OAI-PMH endpoint at research-management.mq.edu.au, which serves 114,062 publication records and a person registry over OAI-PMH 2.0 with five metadata formats and no authentication. Beyond it, Macquarie operates a Shibboleth SAML identity provider registered in the Australian Access Federation, a self-hosted Moodle (iLearn) whose web services are credential-gated, and a public library GitHub organisation whose code consumes Ex Libris Alma rather than exposing anything. Everything else that looks like a Macquarie API is a vendor''s contract running under Macquarie''s name — Figshare for the research data repository, Elsevier Pure
  for the research portal, CourseLoop for the course handbook, Ex Libris Primo for library discovery. Those relationships are recorded here as tenant surfaces; the vendors'' contracts are not.'
examples:
- key_count: 6
  name: Macquarie Oai Pmh Examples
  slug: macquarie-oai-pmh-examples
finops:
- name: Macquarie Finops
  service_category: Education
  slug: macquarie-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/macquarie.png
layout: provider
modified: '2026-08-30'
name: Macquarie University
nav: Providers
network: true
overview: 'Macquarie University publishes 1 API on the [APIs.io](https://apis.io/) network: Research Portal OAI-PMH. Tagged areas include University, Higher Education, Education, Australia, and Group of Eight Peer.


  The Macquarie University catalog on APIs.io includes 1 Spectral governance ruleset.


  Macquarie University''s developer surface includes documentation, support, authentication, and 18 more developer resources.'
plans:
- name: Macquarie Plans Pricing
  plan_count: 2
  slug: macquarie-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Macquarie Rate Limits
  slug: macquarie-rate-limits
rules:
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Macquarie University API Rules
  rule_count: 6
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 1
  slug: macquarie-oai-pmh-spectral-rules
score:
  band: developing
  composite: 44.0
  coverage:
    artifact_dirs: 13
    catalog_gap: 55.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -1.3
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 26.5
    contract_quality: 55.0
    developer_ergonomics: 26.2
    discoverability: 59.3
    governance: 26.5
    operational_transparency: 23.7
  previous_composite: 45.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/macquarie/refs/heads/main/screenshots/macquarie-2026-06-20T184829.png
security:
- kind: authentication
  name: Macquarie Authentication
  slug: macquarie-authentication
  summary_line: none · 1 scheme
- kind: domain-security
  name: Macquarie Domain Security
  slug: macquarie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: macquarie
tags:
- University
- Higher Education
- Education
- Australia
- Group of Eight Peer
- Research Data
- Research Repository
- Metadata Harvesting
- OAI-PMH
- Identity Federation
- Library
- Course Catalog
website: https://www.mq.edu.au/
---
