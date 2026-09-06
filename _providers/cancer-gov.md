---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 29.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Cancer Gov Agentic Access
  operation_count: 6
  slug: cancer-gov-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 9
apis:
- description: RESTful API that lets developers build applications, search tools, and digital platforms over NCI-supported cancer clinical trials data sourced from NCI's Clinical Trials Reporting Program (CTRP). The
  name: NCI Clinical Trials Search API
  slug: clinical-trials-api
- description: 'The external-facing REST interface for the NCI Genomic Data Commons. Drives the GDC Data Portal and GDC Submission Portal and is open for programmatic access. Provides query, download, and submission '
  name: NCI Genomic Data Commons (GDC) API
  slug: gdc-api
- baseURL: https://api.seer.cancer.gov
  baseurl_source: declared
  description: RESTful API for the Surveillance, Epidemiology, and End Results (SEER) Program. Supports SEER datasets plus staging APIs for cancer staging (TNM and Collaborative Stage algorithms), enabling developer
  name: NCI SEER API
  slug: seer-api
- baseURL: https://modac.cancer.gov
  baseurl_source: declared
  description: The NCI Model and Data Clearinghouse (MoDaC) API provides programmatic access to cancer research data, computational models, and associated tools hosted in MoDaC. Developers can search, retrieve metad
  name: NCI MoDaC API
  slug: modac-api
- baseURL: https://api-evsrest.nci.nih.gov
  baseurl_source: declared
  description: 'Enterprise Vocabulary Services (EVS) exposes NCI Thesaurus and NCI Metathesaurus content — over 192,000 concepts, 154,000 textual definitions, 623,000 synonyms and 630,000 inter-concept relationships '
  name: NCI EVS Terminology API
  slug: evs-api
- description: A suite of syndicated content channels — RSS feeds, the NCI Dictionary Widget, and syndicated publication content — that partner sites and health platforms can embed to deliver authoritative cancer co
  name: NCI Content Syndication Services
  slug: syndication-services
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The Diseases API from Cancer.gov — 1 operation(s) for diseases.
  name: Cancer.gov Diseases API
  slug: cancer-gov-diseases-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The Interventions API from Cancer.gov — 1 operation(s) for interventions.
  name: Cancer.gov Interventions API
  slug: cancer-gov-interventions-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The Terms API from Cancer.gov — 1 operation(s) for terms.
  name: Cancer.gov Terms API
  slug: cancer-gov-terms-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The Trials API from Cancer.gov — 2 operation(s) for trials.
  name: Cancer.gov Trials API
  slug: cancer-gov-trials-api
- baseURL: https://webapis.cancer.gov/glossary/v1
  baseurl_source: declared
  description: Serves the NCI Dictionary of Cancer Terms — the authoritative plain-language and health-professional definitions used across cancer.gov and by the NCI Dictionary Widget. Supports autosuggest, full-tex
  name: NCI Glossary Term API
  slug: glossary-api
- baseURL: https://webapis.cancer.gov/drugdictionary/v1
  baseurl_source: declared
  description: Serves the NCI Drug Dictionary — definitions of drugs and drug combinations used in cancer treatment and prevention, matched across generic names, brand names and code names. Supports autosuggest, sea
  name: NCI Drug Dictionary API
  slug: drug-dictionary-api
- baseURL: https://webapis.cancer.gov/sitewidesearch/v1
  baseurl_source: declared
  description: 'The search service behind cancer.gov''s own site search: full-text search and autosuggest across NCI web content, with per-collection scoping and status reporting. No credential required.'
  name: Cancer.gov Site-Wide Search API
  slug: sitewide-search-api
- baseURL: https://webapis.cancer.gov/bestbets/v1
  baseurl_source: declared
  description: Returns NCI's editorially curated 'best bet' results for a search term — the promoted, hand-picked answers cancer.gov surfaces above algorithmic search results. No credential required.
  name: Cancer.gov Best Bets API
  slug: best-bets-api
- baseURL: https://webapis.cancer.gov/r4r/v1
  baseurl_source: declared
  description: Backs NCI's Resources for Researchers directory — searchable metadata about NCI tools, datasets, repositories and services available to the cancer research community. No credential required.
  name: NCI Resources for Researchers API
  slug: r4r-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NCI Clinical Trials Search Diseases API
  slug: open-cancer-gov-diseases-api
- collection_type: open
  name: NCI Clinical Trials Search Diseases Interventions API
  slug: open-cancer-gov-interventions-api
- collection_type: open
  name: NCI Clinical Trials Search Diseases Terms API
  slug: open-cancer-gov-terms-api
- collection_type: open
  name: NCI Clinical Search Diseases Trials API
  slug: open-cancer-gov-trials-api
- collection_type: open
  name: NCI Clinical Trials Search API
  slug: open-cancer-gov
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cancer-gov-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cancer-gov-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cancer-gov-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cancer-gov-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NCIOCPL
- group: company
  title: ''
  type: Website
  url: https://www.cancer.gov/
- group: other
  title: ''
  type: SyndicationServices
  url: https://www.cancer.gov/syndication
- group: other
  title: ''
  type: DataScience
  url: https://datascience.cancer.gov/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cancer.gov/policies/privacy-security
- group: other
  title: ''
  type: LicensingAndReuse
  url: https://www.cancer.gov/policies/copyright-reuse
- group: company
  title: ''
  type: Blog
  url: https://www.cancer.gov/publishedcontent/rss/news-events/cancer-currents-blog.rss
- group: build
  title: ''
  type: Packages
  url: packages/cancer-gov-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cancer-gov-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/cancer-gov-cli.yml
- group: design
  title: ''
  type: Components
  url: components/cancer-gov-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cancer-gov-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cancer-gov-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cancer-gov-llms.txt
- group: docs
  title: ''
  type: GraphQL
  url: graphql/cancer-gov-gdc.graphql
- group: design
  title: ''
  type: Conformance
  url: conformance/cancer-gov-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cancer-gov-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cancer-gov-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://api.gdc.cancer.gov/status
- group: design
  title: ''
  type: Conventions
  url: conventions/cancer-gov-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cancer-gov-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cancer-gov-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cancer-gov-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cancer-gov-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cancer-gov-seer-overlay.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gdc.cancer.gov/API/Users_Guide/Getting_Started/
- group: docs
  title: ''
  type: APIReference
  url: https://api.seer.cancer.gov/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.cancer.gov/syndication/api
- group: start
  title: ''
  type: SignUp
  url: https://clinicaltrialsapi.cancer.gov/
- group: operate
  title: ''
  type: Support
  url: https://www.cancer.gov/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://api.seer.cancer.gov/terms
- group: other
  title: ''
  type: Policies
  url: https://www.cancer.gov/policies
- group: other
  title: ''
  type: OpenDataPolicy
  url: https://datascience.cancer.gov/data-sharing
- group: company
  title: ''
  type: News
  url: https://www.cancer.gov/news-events
created: '2024-07-02'
description: Cancer.gov is the web presence of the National Cancer Institute (NCI), the U.S. federal government's principal agency for cancer research and training. NCI and its partner programs expose a rich set of open APIs covering cancer clinical trials, genomic data, cancer-incidence surveillance, research data and models, terminology and vocabularies, and PDQ content — giving researchers, advocacy groups, clinicians, and application developers programmatic access to authoritative cancer data and content.
finops:
- name: Cancer Gov Finops
  service_category: API
  slug: cancer-gov-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cancer-gov.png
layout: provider
mcp_servers:
- description: ''
  name: Cancer.gov MCP Server
  slug: cancergov-mcp-server
modified: '2026-09-05'
name: Cancer.gov
nav: Providers
network: true
overview: 'Cancer.gov publishes 12 APIs on the [APIs.io](https://apis.io/) network, including NCI SEER API, NCI MoDaC API, NCI EVS Terminology API, and 9 more. Tagged areas include Cancer, Federal-Government, Healthcare, Research, and Clinical Trials.


  Cancer.gov''s developer surface includes authentication, engineering blog, CLI, changelog, documentation, API reference, signup flow, and 32 more developer resources.'
plans:
- name: Cancer Gov Plans Pricing
  plan_count: 1
  slug: cancer-gov-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Cancer Gov Rate Limits
  slug: cancer-gov-rate-limits
score:
  band: developing
  composite: 52.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 58.0
    catalog_earned_first_party: 20.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 16.1
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 41.5
    developer_ergonomics: 61.3
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 36.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/screenshots/cancer-gov-2026-06-20T173920.png
security:
- kind: authentication
  name: Cancer Gov Authentication
  slug: cancer-gov-authentication
  summary_line: apiKey/none · 5 schemes
- kind: domain-security
  name: Cancer Gov Domain Security
  slug: cancer-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cancer-gov
tags:
- Cancer
- Federal-Government
- Healthcare
- Research
- Clinical Trials
- Genomics
- Surveillance
- Open Data
website: https://www.cancer.gov/
---
