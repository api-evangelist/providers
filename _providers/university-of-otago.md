---
access_model:
  confidence: high
  label: Free · one keyless read surface · repository and LMS APIs gated
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-09-01'
api_count: 5
apis:
- description: The University's AI guidance site runs on WordPress that Otago self-hosts on its own domain behind Cloudflare, and it exposes the full WordPress REST API without credentials. Confirmed live 2026-08-30
  name: Artificial Intelligence at Otago — WordPress REST API
  slug: ai-site-wp-rest
- description: OUR Archive (Otago University Research Archive) is the University's institutional research repository. The DATA, the DOIs and the curation are Otago's; the CONTRACT and the engineering are Ex Libris /
  name: OUR Archive OAI-PMH Metadata — Ex Libris Esploro tenancy
  slug: our-archive-oai
- description: The University's learning management system runs on Anthology Blackboard Learn at blackboard.otago.ac.nz, which CNAMEs to otago.blackboard.com and on to AWS ap-southeast-2. The tenancy, roster and cou
  name: Blackboard Learn — University of Otago tenancy
  slug: blackboard-learn
- description: Otago's SAML 2.0 identity is published as a complete IDPSSODescriptor in the SIGNED Tuakiri NZ Access Federation metadata aggregate, under entityID https://idp.otago.ac.nz/idp/shibboleth with DisplayN
  name: University of Otago Identity Provider (SAML 2.0 / Shibboleth) — Tuakiri Hosted Login
  slug: tuakiri-idp
- description: Otago's persistent-identifier registrations, readable through each registry's public REST API. Confirmed live 2026-08-30. DataCite carries provider `otagouni` — "University of Otago", memberType conso
  name: Otago Scholarly Identifier Registrations (DataCite + Crossref)
  slug: scholarly-identifiers
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://www.otago.ac.nz/
- group: other
  title: ''
  type: ResearchRepository
  url: https://ourarchive.otago.ac.nz/
- group: other
  title: ''
  type: IdentityFederation
  url: https://directory.tuakiri.ac.nz/metadata/tuakiri-metadata-signed.xml
- group: other
  title: ''
  type: IdentityFederation
  url: https://docs.tuakiri.ac.nz/
- group: docs
  title: ''
  type: APIReference
  url: https://artificialintelligence.otago.ac.nz/wp-json/
- group: other
  title: ''
  type: AIPolicy
  url: https://artificialintelligence.otago.ac.nz/
- group: other
  title: ''
  type: AIPolicy
  url: https://otago.libguides.com/Generative_AI/policies
- group: other
  title: ''
  type: AIPolicy
  url: https://ask.otago.ac.nz/knowledgebase/article/KA-10005970/en-us
- group: operate
  title: ''
  type: Support
  url: https://ask.otago.ac.nz/
- group: auth
  title: ''
  type: Authentication
  url: https://ask.otago.ac.nz/knowledgebase/article/KA-10002700/en-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-otago/
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-otago-education-standards.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-otago-authentication.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-otago-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: examples/university-of-otago-examples.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-otago-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-otago-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-otago-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-otago-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-otago-context.jsonld
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Otago — Te Whare Wānanga o Ōtākou — is New Zealand''s oldest university, founded in 1869 in Dunedin and registered as https://ror.org/01jmxt844. It operates no public developer program: there is no developer portal, no API reference, no open-data portal and no OpenAPI published under any otago.ac.nz path found in this run. Exactly ONE machine-readable surface is both on Otago''s own domain and operated by Otago — the self-hosted WordPress REST API behind its AI guidance site at artificialintelligence.otago.ac.nz, which serves a 144-route discovery document and published content keyless. Everything else that carries an Otago name is a vendor contract running under it: OUR Archive at ourarchive.otago.ac.nz is an Ex Libris / Clarivate Esploro tenancy (the hostname is Otago''s, the CNAME goes to ap02.esploro.exlibrisgroup.com) whose OAI-PMH endpoint is deployed but refuses public harvesting with error_code 21; blackboard.otago.ac.nz is an Anthology Blackboard
  Learn tenancy running release 4000.21.0 whose REST API answers 401 to everything but a version check; and Otago''s SAML 2.0 identity is published in the signed Tuakiri NZ Access Federation metadata under entityID https://idp.otago.ac.nz/idp/shibboleth while every one of its SSO bindings actually resolves to REANNZ''s Tuakiri Hosted Login service. Otago''s scholarly identifier registrations are real and institution-attributed — DataCite provider otagouni with 334 DOIs in OUR Archive, and Crossref member 4843 "University of Otago Library" holding prefix 10.11157 with 2,537 DOIs. This profile is deliberately thin because the footprint is thin, and the surfaces that exist are recorded under the operator that actually runs them.'
examples:
- key_count: 1
  name: University Of Otago Blackboard Version Response
  slug: university-of-otago-blackboard-version-response
- key_count: 14
  name: University Of Otago Wp Rest Root Response
  slug: university-of-otago-wp-rest-root-response
finops:
- name: University Of Otago Finops
  service_category: Education
  slug: university-of-otago-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-otago.png
jsonld:
- class_count: 8
  name: University Of Otago Context
  property_count: 3
  slug: university-of-otago-context
layout: provider
modified: '2026-08-30'
name: University of Otago
nav: Providers
network: true
overview: 'University of Otago publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, New Zealand, and Research.


  The University of Otago catalog on APIs.io includes 1 JSON-LD context.


  University of Otago''s developer surface includes API reference, support, authentication, code examples, engineering blog, and 17 more developer resources.'
plans:
- name: University Of Otago Plans Pricing
  plan_count: 2
  slug: university-of-otago-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: University Of Otago Rate Limits
  slug: university-of-otago-rate-limits
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 11
    catalog_gap: 43.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 15.2
    contract_quality: 17.3
    developer_ergonomics: 35.7
    discoverability: 74.1
    governance: 15.2
    operational_transparency: 21.1
  previous_composite: 29.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-otago/refs/heads/main/screenshots/university-of-otago-2026-06-20T200216.png
security:
- kind: authentication
  name: University Of Otago Authentication
  slug: university-of-otago-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Otago Domain Security
  slug: university-of-otago-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-otago
tags:
- University
- Higher Education
- Education
- New Zealand
- Research
- Research Repository
- Open Access
- Repository
- Identity Federation
- Shibboleth
- SAML
- OAI-PMH
- Learning Management
- DataCite
- Crossref
- Metadata
- Library
website: https://www.otago.ac.nz/
---
