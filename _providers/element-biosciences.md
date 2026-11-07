---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Element Biosciences Agentic Access
  operation_count: 16
  slug: element-biosciences-agentic-access
  summary_line: 16 operations
api_count: 1
apis:
- baseURL: https://cloud-api.usw2.elembio.io
  baseurl_source: declared
  description: ExecutionService provides access to workflow executions — runs of a bioinformatics workflow that process instrument data. Listing and reading execution metadata requires the "executions:read" scope; l
  name: Element Biosciences Execution Service API
  slug: element-biosciences-executionservice-api
- baseURL: https://cloud-api.usw2.elembio.io
  baseurl_source: declared
  description: InstrumentService provides access to instruments registered to the authenticated tenant. Requires the "instruments:read" scope.
  name: Element Biosciences Instrument Service API
  slug: element-biosciences-instrumentservice-api
- baseURL: https://cloud-api.usw2.elembio.io
  baseurl_source: declared
  description: RunService provides access to instrument runs, both sequencing and multiomics. Listing and reading run metadata requires the "runs:read" scope; listing run files and obtaining download credentials req
  name: Element Biosciences Run Service API
  slug: element-biosciences-runservice-api
- baseURL: https://cloud-api.usw2.elembio.io
  baseurl_source: declared
  description: 'StorageConnectionService provides access to storage connections: their metadata (requires the "storage:read" scope) and the files within them (ListFiles / GetDownloadCredentials, which require the "st'
  name: Element Biosciences Storage Connection Service API
  slug: element-biosciences-storageconnectionservice-api
- baseURL: https://cloud-api.usw2.elembio.io
  baseurl_source: declared
  description: AuthService reports information about the API key making the request.
  name: Element Biosciences Auth Service API
  slug: element-biosciences-auth-service-api
artifact_total: 19
collections:
- collection_type: open
  name: Element Biosciences Cloud Auth Service API
  slug: open-element-biosciences-authservice-api
- collection_type: open
  name: Element Biosciences Cloud Execution Service API
  slug: open-element-biosciences-executionservice-api
- collection_type: open
  name: Element Biosciences Cloud Instrument Service API
  slug: open-element-biosciences-instrumentservice-api
- collection_type: open
  name: Element Biosciences Cloud Run Service API
  slug: open-element-biosciences-runservice-api
- collection_type: open
  name: Element Biosciences Cloud Storage Connection Service API
  slug: open-element-biosciences-storageconnectionservice-api
common:
- group: other
  href: https://artifacts.apis.io/element-biosciences/overlays/element-biosciences-cloud-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/element-biosciences-cloud-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/element-biosciences/agentic-access/element-biosciences-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/element-biosciences-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.elementbiosciences.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.elembio.io/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.elembio.io/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.elembio.io/developers/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.elembio.io/developers/api/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://www.elementbiosciences.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.elementbiosciences.com/knowledge-base
- group: company
  title: ''
  type: Blog
  url: https://www.elementbiosciences.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Elembio
- group: start
  title: ''
  type: SignUp
  url: https://cloud.elembio.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.elementbiosciences.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.elementbiosciences.com/legal/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.elembio.io/developers/api/api-changelog/
- group: operate
  href: https://artifacts.apis.io/element-biosciences/changelog/element-biosciences-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/element-biosciences-changelog.yml
- group: auth
  href: https://artifacts.apis.io/element-biosciences/authentication/element-biosciences-authentication.yml
  title: ''
  type: Authentication
  url: authentication/element-biosciences-authentication.yml
- group: auth
  href: https://artifacts.apis.io/element-biosciences/scopes/element-biosciences-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/element-biosciences-scopes.yml
- group: design
  href: https://artifacts.apis.io/element-biosciences/conventions/element-biosciences-conventions.yml
  title: ''
  type: Conventions
  url: conventions/element-biosciences-conventions.yml
- group: design
  href: https://artifacts.apis.io/element-biosciences/errors/element-biosciences-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/element-biosciences-problem-types.yml
- group: design
  href: https://artifacts.apis.io/element-biosciences/lifecycle/element-biosciences-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/element-biosciences-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/element-biosciences/conformance/element-biosciences-conformance.yml
  title: ''
  type: Conformance
  url: conformance/element-biosciences-conformance.yml
- group: design
  href: https://artifacts.apis.io/element-biosciences/data-model/element-biosciences-data-model.yml
  title: ''
  type: DataModel
  url: data-model/element-biosciences-data-model.yml
- group: build
  href: https://artifacts.apis.io/element-biosciences/packages/element-biosciences-packages.yml
  title: ''
  type: Packages
  url: packages/element-biosciences-packages.yml
- group: build
  href: https://artifacts.apis.io/element-biosciences/packages/element-biosciences-packages.yml
  title: ''
  type: SDKs
  url: packages/element-biosciences-packages.yml
- group: build
  href: https://artifacts.apis.io/element-biosciences/cli/element-biosciences-cli.yml
  title: ''
  type: CLI
  url: cli/element-biosciences-cli.yml
- group: agent
  href: https://artifacts.apis.io/element-biosciences/well-known/element-biosciences-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/element-biosciences-well-known.yml
- group: agent
  href: https://artifacts.apis.io/element-biosciences/llms/element-biosciences-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/element-biosciences-llms.txt
- group: agent
  href: https://artifacts.apis.io/element-biosciences/mcp/element-biosciences-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/element-biosciences-mcp.yml
- group: build
  href: https://artifacts.apis.io/element-biosciences/mcp/element-biosciences-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/element-biosciences-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/element-biosciences/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/element-biosciences/security/element-biosciences-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/element-biosciences-domain-security.yml
- group: other
  title: ''
  type: Forge
  url: https://forgeglobal.com/element-biosciences_stock/
created: '2026-08-04'
description: Element Biosciences is a San Diego based life-sciences instrumentation company that builds benchtop DNA sequencing and multiomics systems — the AVITI, AVITI LT, AVITI24 and VITARI platforms — around its proprietary Avidite Base Chemistry (ABC), which decouples signal generation from nucleotide incorporation to deliver high-accuracy base calling at lower cost than conventional sequencing-by-synthesis. Instrument output is managed through ElemBio Cloud, the company's analysis and data-management platform, which runs bioinformatics workflows such as Bases2Fastq and Cells2Stats and streams run data into customer-owned cloud storage connections. ElemBio Cloud exposes a public, versioned REST API — the Element Biosciences Cloud API — plus a first-party cross-platform CLI, giving labs programmatic access to sequencing and multiomics runs, workflow executions, registered instruments, storage connections and the files those resources produce, for dashboards, fleet monitoring, LIMS read-back
  and custom automation.
image: https://www.elementbiosciences.com/hubfs/Element%20Biosciences%202025/Image/Hero_Home_Logo.svg
layout: provider
modified: '2026-08-04'
name: Element Biosciences
nav: Providers
network: true
overview: 'Element Biosciences publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Execution Service API, Instrument Service API, Run Service API, and 2 more. Tagged areas include Company, Genomics, DNA Sequencing, Life Sciences, and Bioinformatics.


  The Element Biosciences catalog on APIs.io includes 1 Spectral governance ruleset.


  Element Biosciences'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 26 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Element Biosciences API Rules
  rule_count: 65
  severity_counts:
    error: 57
    hint: 0
    info: 3
    warn: 5
  slug: element-biosciences-rules
scopes:
- name: Element Biosciences Scopes
  scope_count: 12
  slug: element-biosciences-scopes
  summary_line: 12 scopes
score:
  band: developing
  composite: 50.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 58.8
    developer_ergonomics: 73.2
    discoverability: 66.1
    operational_transparency: 18.4
  previous_composite: 49.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/element-biosciences/element-biosciences-2026-08-07T164822.png
security:
- kind: authentication
  name: Element Biosciences Authentication
  slug: element-biosciences-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Element Biosciences Domain Security
  slug: element-biosciences-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: Audit what an ElemBio Cloud API key can reach
  slug: element-biosciences-audit-api-key-access
- name: Find a completed run and download its files
  slug: element-biosciences-find-and-download-run-files
- name: Monitor the Element Biosciences sequencing fleet
  slug: element-biosciences-monitor-sequencing-fleet
- name: Triage a failed ElemBio Cloud analysis execution
  slug: element-biosciences-triage-failed-execution
slug: element-biosciences
tags:
- Company
- Genomics
- DNA Sequencing
- Life Sciences
- Bioinformatics
- Multiomics
- Laboratory
- Scientific Instruments
- Cloud Storage
- Biotechnology
website: https://www.elementbiosciences.com/
---
