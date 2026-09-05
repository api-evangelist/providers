---
access_model:
  confidence: high
  label: Free · no key required
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
    agentic_access: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Charles Agentic Access
  operation_count: 7
  slug: charles-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 5
apis:
- baseURL: https://lindat.mff.cuni.cz/services/translation/api/v2
  baseurl_source: declared
  description: Source and target language operations of the LINDAT Machine Translation API, operated by the Institute of Formal and Applied Linguistics (UFAL) at Charles University. Translation is performed by posti
  name: LINDAT Translation Languages API
  slug: charles-languages-api
- baseURL: https://lindat.mff.cuni.cz/services/translation/api/v2
  baseurl_source: declared
  description: Translation-model operations of the LINDAT Machine Translation API, operated by UFAL at Charles University. Models are neural MT systems such as CUBBITT, addressed by source-target code.
  name: LINDAT Translation Models API
  slug: charles-models-api
- baseURL: https://lindat.mff.cuni.cz/services/translation/api/v2
  baseurl_source: declared
  description: Root navigation resource of the LINDAT Machine Translation API, returning HAL links to the languages and models collections.
  name: LINDAT Translation Root API
  slug: charles-root-api
- baseURL: https://lindat.mff.cuni.cz/services/udpipe/api
  baseurl_source: declared
  description: Public keyless REST API for tokenization, part-of-speech tagging, lemmatization and dependency parsing of CoNLL-U data, operated by UFAL at Charles University. The live service advertised 961 Universa
  name: LINDAT UDPipe API
  slug: lindat-udpipe
- baseURL: https://lindat.mff.cuni.cz/services/nametag/api
  baseurl_source: declared
  description: Public keyless REST API for named-entity recognition and tokenization (NameTag 3) operated by UFAL at Charles University via LINDAT/CLARIAH-CZ. The OpenAPI here is derived by API Evangelist from the s
  name: LINDAT NameTag API
  slug: lindat-nametag
- baseURL: https://lindat.mff.cuni.cz/services/morphodita/api
  baseurl_source: declared
  description: Public keyless REST API for morphological analysis, morphological generation, part-of-speech tagging and tokenization, principally for Czech, operated by UFAL at Charles University. The OpenAPI here i
  name: LINDAT MorphoDiTa API
  slug: lindat-morphodita
- baseURL: https://lindat.mff.cuni.cz/services/korektor/api
  baseurl_source: declared
  description: Public keyless REST API for Czech statistical spellchecking, diacritics generation and ranked correction suggestions, operated by UFAL at Charles University. The OpenAPI here is derived by API Evangel
  name: LINDAT Korektor API
  slug: lindat-korektor
- description: The Charles University Digital Repository (Digitalni repozitar UK), a DSpace instance running on university-owned infrastructure (dspace.cuni.cz resolves to dspace-in-1.is.cuni.cz), exposes a public O
  name: CU Digital Repository OAI-PMH
  slug: digital-repository-oai
- description: The Charles University Research Publications Repository (Repozitar publikacni cinnosti UK), a DSpace instance on university-owned infrastructure, exposes a public OAI-PMH 2.0 endpoint for metadata har
  name: CU Research Publications Repository OAI-PMH
  slug: publications-repository-oai
- description: OAI-PMH 2.0 endpoint of the LINDAT/CLARIAH-CZ digital library operated by UFAL at Charles University, holding language resources and tools back to 2006. The Identify response also carries an olac-arch
  name: LINDAT/CLARIAH-CZ Repository OAI-PMH
  slug: lindat-repository-oai
- description: DSpace 7 HAL+JSON REST API of the LINDAT/CLARIAH-CZ digital library, served from UFAL's own host at Charles University. The root discovery document returns 200 application/hal+json; item collections r
  name: LINDAT/CLARIAH-CZ Repository REST API
  slug: lindat-repository-rest
- description: 'Charles University operates its own Shibboleth SAML 2.0 identity provider. Metadata is served at idp.cuni.cz as application/xml with entityID https://cas.cuni.cz/idp/shibboleth, shibmd:Scope cuni.cz, '
  name: Charles University Shibboleth Identity Provider
  slug: identity-provider
- description: Charles University is a DataCite registrant under provider symbol CUNI, memberType consortium_organization, country CZ, linked to ROR https://ror.org/024d6js02. This is a membership record — a fact ab
  name: DataCite Registrant — Charles University (CUNI)
  slug: datacite-membership
- description: 'Charles University holds two Crossref memberships: 5727, "Charles University in Prague, Karolinum Press" (the university press), and 55007, the Institute of Communication Studies and Journalism in the'
  name: Crossref Membership — Charles University
  slug: crossref-membership
- description: Charles University is registered in the Research Organization Registry as https://ror.org/024d6js02, located in Czechia. Recorded as a registry membership; the ROR API is ROR's own.
  name: ROR Registration — Charles University
  slug: ror-registration
- description: UKAZ, the Charles University library discovery service, is an Ex Libris Primo VE tenancy. ukaz.cuni.cz redirects to cuni.primo.exlibrisgroup.com with institution view id 420CKIS_INST:UKAZ. The tenancy
  name: UKAZ Library Discovery — Ex Libris Primo VE tenancy
  slug: library-discovery-primo
- description: cuni.figshare.com is a Figshare tenancy for Charles University; DNS resolves it by CNAME to figshare.com. The host answered an AWS WAF bot challenge (HTTP 202, empty body) on 2026-09-01, so the tenanc
  name: Charles University Figshare — Figshare tenancy
  slug: figshare-repository
artifact_total: 42
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LINDAT Translation languages API
  slug: open-charles-languages-api
- collection_type: open
  name: LINDAT Translation languages models API
  slug: open-charles-models-api
- collection_type: open
  name: LINDAT Translation languages root API
  slug: open-charles-root-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.cuni.cz/UKEN-1.html
- group: docs
  title: ''
  type: Documentation
  url: https://lindat.mff.cuni.cz/en/services
- group: docs
  title: ''
  type: APIReference
  url: https://lindat.mff.cuni.cz/services/udpipe/api-reference.php
- group: other
  title: ''
  type: ResearchRepository
  url: https://lindat.mff.cuni.cz/repository/xmlui/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://ukaz.cuni.cz/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://is.cuni.cz/studium/eng/index.php
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.cuni.cz/idp/shibboleth
- group: other
  title: ''
  type: AIPolicy
  url: https://ai.cuni.cz/AI-36.html
- group: build
  title: ''
  type: AITooling
  url: https://ai.cuni.cz/AI-9.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lindat.mff.cuni.cz/en/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://lindat.mff.cuni.cz/user_feedback
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ufal
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UKUK-Repository-Dept
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/univerzita-karlova/
- group: auth
  title: ''
  type: Authentication
  url: https://uvt.cuni.cz/UVTEN-37.html
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.cuni.cz/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/charles-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/charles-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/charles-agentic-access.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/charles-education-standards-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/charles-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/charles-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/charles-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: Charles University (Univerzita Karlova), founded in 1348 in Prague, is the largest and oldest university in Czechia. Unusually for a university, a substantial part of its programmable footprint is genuinely institution-operated rather than a vendor contract running under its name. The Institute of Formal and Applied Linguistics (UFAL) in the Faculty of Mathematics and Physics runs the LINDAT/CLARIAH-CZ research infrastructure and publishes five documented, keyless, production REST APIs on its own host — machine translation, UDPipe (tokenization, tagging, lemmatization and dependency parsing across 961 Universal Dependencies models), NameTag (named-entity recognition), MorphoDiTa (morphological analysis and generation) and Korektor (Czech spellchecking and diacritics). Three DSpace repositories on university-owned infrastructure expose OAI-PMH 2.0, and the LINDAT repository additionally exposes a DSpace 7 HAL REST API. The university operates its own Shibboleth SAML identity
  provider at idp.cuni.cz, registered in the Czech national federation eduID.cz, and is a DataCite registrant (CUNI) and Crossref member. What it does NOT have is a central developer portal, an open-data portal, or any public API over the Study Information System (SIS) or student records — those are gated behind eduID/Shibboleth. Library discovery (UKAZ) is an Ex Libris Primo tenancy and cuni.figshare.com is a Figshare tenancy; both are real institutional relationships whose contracts belong to the vendors.
examples:
- key_count: 4
  name: Charles Get Language Collection Example
  slug: charles-get-language-collection-example
- key_count: 4
  name: Charles Get Model Collection Example
  slug: charles-get-model-collection-example
- key_count: 7
  name: Charles Korektor Suggestions Example
  slug: charles-korektor-suggestions-example
- key_count: 7
  name: Charles Morphodita Tag Example
  slug: charles-morphodita-tag-example
- key_count: 7
  name: Charles Nametag Models Example
  slug: charles-nametag-models-example
- key_count: 7
  name: Charles Nametag Recognize Example
  slug: charles-nametag-recognize-example
- key_count: 4
  name: Charles Post Model Item Example
  slug: charles-post-model-item-example
- key_count: 7
  name: Charles Udpipe Process Example
  slug: charles-udpipe-process-example
finops:
- name: Charles Finops
  service_category: Education
  slug: charles-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/charles.png
json_schemas:
- name: LanguageResource
  property_count: 3
  slug: charles-language
- name: ModelResource
  property_count: 6
  slug: charles-model
json_structures:
- name: Charles Language Structure
  property_count: 2
  slug: charles-language-structure
- name: Charles Model Structure
  property_count: 5
  slug: charles-model-structure
jsonld:
- class_count: 8
  name: Charles Context
  property_count: 3
  slug: charles-context
layout: provider
modified: '2026-09-01'
name: Charles University
nav: Providers
network: true
overview: 'Charles University publishes 7 APIs on the [APIs.io](https://apis.io/) network, including LINDAT Translation Languages API, LINDAT Translation Models API, LINDAT Translation Root API, and 4 more. Tagged areas include University, Higher Education, Education, Research, and Czechia.


  The Charles University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Charles University''s developer surface includes documentation, API reference, support, GitHub presence, authentication, and 19 more developer resources.'
plans:
- name: Charles Plans Pricing
  plan_count: 2
  slug: charles-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Charles Rate Limits
  slug: charles-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Charles University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: charles-jsonschema-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Charles University API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 3
  slug: charles-rules
score:
  band: developing
  composite: 44.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 70.3
    catalog_earned_first_party: 0.0
    catalog_gap: 44.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 52.6
    developer_ergonomics: 33.3
    discoverability: 85.2
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 44.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/charles/refs/heads/main/screenshots/charles-2026-06-20T174227.png
security:
- kind: domain-security
  name: Charles Domain Security
  slug: charles-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Charles Vulnerability Disclosure
  slug: charles-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: charles
tags:
- University
- Higher Education
- Education
- Research
- Czechia
- Europe
- Language Technology
- Natural Language Processing
- Machine Translation
- Research Repository
- Identity Federation
- OAI-PMH
- CLARIN
website: https://www.cuni.cz/UKEN-1.html
---
