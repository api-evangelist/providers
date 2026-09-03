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
  scored_at: '2026-09-02'
api_count: 3
apis:
- baseURL: https://data.southampton.ac.uk/
  baseurl_source: declared
  description: 'Institution-built, institution-hosted linked open data covering the physical and organisational University: buildings and sites, term dates, organisational structure, research facilities, points of se'
  name: University of Southampton Open Data Service (Linked Data)
  slug: open-data-linked-data
- description: The University's own Shibboleth 3.x Identity Provider, entityID https://webauth.soton.ac.uk/shibboleth, asserting shibmd:Scope soton.ac.uk. Its entity descriptor is published both by the IdP itself an
  name: Shibboleth SAML Identity Provider (UK Access Management Federation)
  slug: shibboleth-saml-idp
- baseURL: https://eprints.soton.ac.uk/cgi/oai2
  baseurl_source: declared
  description: 'Live, open OAI-PMH 2.0 metadata harvesting for ePrints Soton, the University''s institutional research repository. Verified 2026-08-30: Identify returned repositoryName ''ePrints Soton'', repositoryIdent'
  name: ePrints Soton OAI-PMH Interface
  slug: eprints-oai-pmh
- baseURL: https://eprints.soton.ac.uk/rest
  baseurl_source: declared
  description: Read-only REST interface over the ePrints Soton data model, exposing the repository's eprint, user and subject datasets. Unauthenticated. Individual records dereference by identifier with a format ext
  name: ePrints Soton REST Interface
  slug: eprints-rest
- description: 'The University''s tenancy of Elsevier Pure, its Current Research Information System, at pure.soton.ac.uk. Pure is now the system of record: researchers deposit into Pure and outputs flow onward to ePri'
  name: Elsevier Pure CRIS tenancy
  slug: pure-cris-tenancy
- description: The University's tenancy of Figshare for research data, at southampton.figshare.com. Live and reachable but fronted by an AWS WAF bot challenge — HTTP 202 with header x-amzn-waf-action:challenge and a
  name: Figshare research data repository tenancy
  slug: figshare-tenancy
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://www.southampton.ac.uk/
- group: other
  title: ''
  type: OpenData
  url: https://data.southampton.ac.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://www.data.southampton.ac.uk/faq.html
- group: other
  title: ''
  type: ResearchRepository
  url: https://eprints.soton.ac.uk/
- group: other
  title: ''
  type: IdentityFederation
  url: http://mdq.ukfederation.org.uk/entities/https%3A%2F%2Fwebauth.soton.ac.uk%2Fshibboleth
- group: other
  title: ''
  type: AIPolicy
  url: https://www.southampton.ac.uk/about/governance/regulations-policies/policies/using-gen-ai-during-your-studies
- group: build
  title: ''
  type: AITooling
  url: https://ai.southampton.ac.uk/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/southampton
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/southampton
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-southampton/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.southampton.ac.uk/about/governance/regulations-policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.southampton.ac.uk/about/governance/information-publications/publication-scheme
- group: operate
  title: ''
  type: Support
  url: https://www.southampton.ac.uk/isolutions/
- group: company
  title: ''
  type: Blog
  url: https://blog.soton.ac.uk/data/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.soton.ac.uk/data/feed/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-southampton-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-southampton-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-southampton-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-southampton-finops.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-southampton-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-southampton-conformance.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-southampton-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/university-of-southampton-rules.yml
- group: design
  title: ''
  type: Errors
  url: errors/university-of-southampton-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-southampton-lifecycle.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/university-of-southampton-scopes.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: x-blogs
  url: blogs/blogs.json
- group: design
  title: ''
  type: x-json-ld
  url: json-ld/university-of-southampton-context.jsonld
created: '2026-06-03'
description: 'The University of Southampton is a public research university in Southampton, United Kingdom, a founding member of the Russell Group and one of the few institutions in this cohort whose programmable footprint is genuinely its own engineering rather than a supplier''s contract running under its name. Four institution-operated surfaces were found and verified by live probe on 2026-08-30. The University of Southampton Open Data Service at data.southampton.ac.uk, with persistent identifiers under id.southampton.ac.uk, publishes twenty-two datasets of campus, building, organisational, catalogue, transport and facilities data as five-star linked data under the Open Government Licence, reachable by content negotiation in Turtle, RDF/XML and N-Triples and by bulk dump per dataset. It is institution-built on tooling Southampton wrote, and it covers the campus-life and timetable classes that universities operate and almost never publish. The University runs its own Shibboleth 3.x SAML
  2.0 Identity Provider, entityID https://webauth.soton.ac.uk/shibboleth, scope soton.ac.uk, registered in the Jisc UK Access Management Federation and reachable through eduGAIN. ePrints Soton, the institutional research repository, exposes a live open OAI-PMH 2.0 interface offering eight metadata formats including RIOXX v2.0, plus a read REST interface over the EPrints data model; the platform is EPrints 3.3.15, software developed at Southampton itself, so uniquely in this cohort neither the host nor the repository software belongs to a vendor. The University is a DataCite member in its own right with 6,735 DOIs minted under its own prefix 10.5258, and a Crossref member under prefix 10.22493. Two further surfaces are real but tenant-operated and are recorded as relationships without holding the supplier''s specification: the Elsevier Pure CRIS tenancy at pure.soton.ac.uk, which is now the system of record for research deposit and whose public web services are switched off, and the Figshare
  research data tenancy at southampton.figshare.com. One prominent claim in the previous profile of this institution is now false and has been withdrawn. The public SPARQL endpoint at sparql.data.southampton.ac.uk is decommissioned: it answers every request with HTTP 200 and the body "Sorry, We no longer off a public SPARQL interface to Southampton Open Data", and the Open Data catalogue''s own VoID metadata still advertises it. There is no central developer portal, no api.southampton.ac.uk and no public course, registrar or research-computing API. Access across the estate is open and standards-based rather than key-gated, and no surface publishes a version, changelog, status page or deprecation signal.'
finops:
- name: University Of Southampton Finops
  service_category: Education
  slug: university-of-southampton-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-southampton.png
jsonld:
- class_count: 6
  name: University Of Southampton Context
  property_count: 8
  slug: university-of-southampton-context
layout: provider
modified: '2026-08-30'
name: University of Southampton
nav: Providers
network: true
overview: 'University of Southampton publishes 3 APIs on the [APIs.io](https://apis.io/) network: Open Data Service (Linked Data), ePrints Soton OAI-PMH Interface, and ePrints Soton REST Interface. Tagged areas include University, Higher Education, Education, Russell Group, and United Kingdom.


  The University of Southampton catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of Southampton''s developer surface includes documentation, support, engineering blog, authentication, and 25 more developer resources.'
plans:
- name: University Of Southampton Plans Pricing
  plan_count: 3
  slug: university-of-southampton-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 4
  name: University Of Southampton Rate Limits
  slug: university-of-southampton-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: University of Southampton API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: university-of-southampton-rules
scopes:
- name: University Of Southampton Scopes
  scope_count: 0
  slug: university-of-southampton-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 17
    catalog_gap: 38.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 3.8
    contract_quality: 20.2
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 3.8
    operational_transparency: 34.2
  previous_composite: 40.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-southampton/refs/heads/main/screenshots/university-of-southampton-2026-06-20T200226.png
security:
- kind: authentication
  name: University Of Southampton Authentication
  slug: university-of-southampton-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Southampton Domain Security
  slug: university-of-southampton-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-southampton
tags:
- University
- Higher Education
- Education
- Russell Group
- United Kingdom
- Open Data
- Linked Data
- Research Repository
- Identity Federation
- OAI-PMH
- Research
- Course Catalog
website: https://www.southampton.ac.uk/
---
