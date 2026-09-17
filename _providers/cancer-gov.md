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
  schema_version: '0.2'
  score: 29.0
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 85
  human_in_the_loop: 32
  name: Cancer Gov Agentic Access
  operation_count: 231
  slug: cancer-gov-agentic-access
  summary_line: 231 operations · 85 acting · 32 human-in-the-loop
api_count: 17
apis:
- description: RESTful API that lets developers build applications, search tools, and digital platforms over NCI-supported cancer clinical trials data sourced from NCI's Clinical Trials Reporting Program (CTRP). The
  name: NCI Clinical Trials Search API
  slug: clinical-trials-api
- description: 'The external-facing REST interface for the NCI Genomic Data Commons. Drives the GDC Data Portal and GDC Submission Portal and is open for programmatic access. Provides query, download, and submission '
  name: NCI Genomic Data Commons (GDC) API
  slug: gdc-api
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
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The Application version endpoint API from Cancer.gov — 1 operation(s) for application version endpoint.
  name: Cancer.gov Application version endpoint API
  slug: cancer-gov-application-version-endpoint-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The asset-details-controller API from Cancer.gov — 1 operation(s) for asset-details-controller.
  name: Cancer.gov Asset Details Controller API
  slug: cancer-gov-asset-details-controller-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The Autosuggest API from Cancer.gov — 4 operation(s) for autosuggest.
  name: Cancer.gov Autosuggest API
  slug: cancer-gov-autosuggest-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The Concept endpoints API from Cancer.gov — 21 operation(s) for concept endpoints.
  name: Cancer.gov Concept endpoints API
  slug: cancer-gov-concept-endpoints-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The delete-collection-controller API from Cancer.gov — 1 operation(s) for delete-collection-controller.
  name: Cancer.gov Delete Collection Controller API
  slug: cancer-gov-delete-collection-controller-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The delete-data-file-controller API from Cancer.gov — 1 operation(s) for delete-data-file-controller.
  name: Cancer.gov Delete Data File Controller API
  slug: cancer-gov-delete-data-file-controller-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The delete-predictions-controller API from Cancer.gov — 1 operation(s) for delete-predictions-controller.
  name: Cancer.gov Delete Predictions Controller API
  slug: cancer-gov-delete-predictions-controller-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: Hematopoietic, lymphoid neoplasms and solid tumor diseases
  name: Cancer.gov Disease API
  slug: cancer-gov-disease-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The doe-collection-controller API from Cancer.gov — 1 operation(s) for doe-collection-controller.
  name: Cancer.gov Doe Collection Controller API
  slug: cancer-gov-doe-collection-controller-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The doe-create-bulk-datafile-controller API from Cancer.gov — 1 operation(s) for doe-create-bulk-datafile-controller.
  name: Cancer.gov Doe Create Bulk Datafile Controller API
  slug: cancer-gov-doe-create-bulk-datafile-controller-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The doe-create-collection-controller API from Cancer.gov — 1 operation(s) for doe-create-collection-controller.
  name: Cancer.gov Doe Create Collection Controller API
  slug: cancer-gov-doe-create-collection-controller-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The doe-create-datafile-controller API from Cancer.gov — 1 operation(s) for doe-create-datafile-controller.
  name: Cancer.gov Doe Create Datafile Controller API
  slug: cancer-gov-doe-create-datafile-controller-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The doe-download-controller API from Cancer.gov — 1 operation(s) for doe-download-controller.
  name: Cancer.gov Doe Download Controller API
  slug: cancer-gov-doe-download-controller-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The doe-download-files-controller API from Cancer.gov — 1 operation(s) for doe-download-files-controller.
  name: Cancer.gov Doe Download Files Controller API
  slug: cancer-gov-doe-download-files-controller-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The doe-retry-download-task-controller API from Cancer.gov — 1 operation(s) for doe-retry-download-task-controller.
  name: Cancer.gov Doe Retry Download Task Controller API
  slug: cancer-gov-doe-retry-download-task-controller-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The doe-retry-uploadtask-controller API from Cancer.gov — 1 operation(s) for doe-retry-uploadtask-controller.
  name: Cancer.gov Doe Retry Uploadtask Controller API
  slug: cancer-gov-doe-retry-uploadtask-controller-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The doe-sync-download-controller API from Cancer.gov — 1 operation(s) for doe-sync-download-controller.
  name: Cancer.gov Doe Sync Download Controller API
  slug: cancer-gov-doe-sync-download-controller-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The Drugs API from Cancer.gov — 6 operation(s) for drugs.
  name: Cancer.gov Drugs API
  slug: cancer-gov-drugs-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: A glossary of cancer-related terms
  name: Cancer.gov Glossary API
  slug: cancer-gov-glossary-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: Healthcare Common Procedure Coding Systems (HCPCS) nomenclatures
  name: Cancer.gov Hcpcs API
  slug: cancer-gov-hcpcs-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The History endpoints API from Cancer.gov — 2 operation(s) for history endpoints.
  name: Cancer.gov History endpoints API
  slug: cancer-gov-history-endpoints-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The home-controller API from Cancer.gov — 1 operation(s) for home-controller.
  name: Cancer.gov Home Controller API
  slug: cancer-gov-home-controller-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The Mapset endpoints API from Cancer.gov — 3 operation(s) for mapset endpoints.
  name: Cancer.gov Mapset endpoints API
  slug: cancer-gov-mapset-endpoints-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The Metadata endpoints API from Cancer.gov — 24 operation(s) for metadata endpoints.
  name: Cancer.gov Metadata endpoints API
  slug: cancer-gov-metadata-endpoints-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: Multiple Primary and Histology Coding Rules
  name: Cancer.gov Mph API
  slug: cancer-gov-mph-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: NAACCR Documentation
  name: Cancer.gov Naaccr API
  slug: cancer-gov-naaccr-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: A searchable mirror of National Drug Codes (NDC)
  name: Cancer.gov Ndc API
  slug: cancer-gov-ndc-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The perform-inferencing-controller API from Cancer.gov — 2 operation(s) for perform-inferencing-controller.
  name: Cancer.gov Perform Inferencing Controller API
  slug: cancer-gov-perform-inferencing-controller-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: Recode algorithms
  name: Cancer.gov Recode API
  slug: cancer-gov-recode-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The release-notes-notifications-controller API from Cancer.gov — 1 operation(s) for release-notes-notifications-controller.
  name: Cancer.gov Release Notes Notifications Controller API
  slug: cancer-gov-release-notes-notifications-controller-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The Resource API from Cancer.gov — 1 operation(s) for resource.
  name: Cancer.gov Resource API
  slug: cancer-gov-resource-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The Resources API from Cancer.gov — 1 operation(s) for resources.
  name: Cancer.gov Resources API
  slug: cancer-gov-resources-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The rest-api-common-controller API from Cancer.gov — 17 operation(s) for rest-api-common-controller.
  name: Cancer.gov Rest API Common Controller API
  slug: cancer-gov-rest-api-common-controller-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: Antineoplastic drugs database
  name: Cancer.gov Rx API
  slug: cancer-gov-rx-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The Search API from Cancer.gov — 2 operation(s) for search.
  name: Cancer.gov Search API
  slug: cancer-gov-search-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The Search endpoint API from Cancer.gov — 4 operation(s) for search endpoint.
  name: Cancer.gov Search endpoint API
  slug: cancer-gov-search-endpoint-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: Staging Algorithms
  name: Cancer.gov Staging API
  slug: cancer-gov-staging-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The Subset endpoints API from Cancer.gov — 3 operation(s) for subset endpoints.
  name: Cancer.gov Subset endpoints API
  slug: cancer-gov-subset-endpoints-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: SEER Site-Specific Surgery Codes
  name: Cancer.gov Surgery API
  slug: cancer-gov-surgery-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The Best Bets API from Cancer.gov — 2 operation(s) for best bets.
  name: Cancer.gov Best Bets API
  slug: cancer-gov-best-bets-api
- baseURL: https://clinicaltrialsapi.cancer.gov/api/v2
  baseurl_source: declared
  description: The Health Check API from Cancer.gov — 1 operation(s) for health check.
  name: Cancer.gov Health Check API
  slug: cancer-gov-health-check-api
artifact_total: 61
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
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/overlays/cancer-gov-modac-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cancer-gov-modac-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/overlays/cancer-gov-evs-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cancer-gov-evs-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/overlays/cancer-gov-glossary-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cancer-gov-glossary-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/overlays/cancer-gov-drug-dictionary-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cancer-gov-drug-dictionary-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/overlays/cancer-gov-sitewide-search-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cancer-gov-sitewide-search-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/overlays/cancer-gov-best-bets-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cancer-gov-best-bets-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/overlays/cancer-gov-r4r-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cancer-gov-r4r-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/capabilities/cancer-gov-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cancer-gov-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/agentic-access/cancer-gov-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cancer-gov-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/security/cancer-gov-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cancer-gov-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/authentication/cancer-gov-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/packages/cancer-gov-packages.yml
  title: ''
  type: Packages
  url: packages/cancer-gov-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/packages/cancer-gov-packages.yml
  title: ''
  type: SDKs
  url: packages/cancer-gov-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/cli/cancer-gov-cli.yml
  title: ''
  type: CLI
  url: cli/cancer-gov-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/components/cancer-gov-components.yml
  title: ''
  type: Components
  url: components/cancer-gov-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/mcp/cancer-gov-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cancer-gov-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/mcp/cancer-gov-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cancer-gov-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/llms/cancer-gov-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cancer-gov-llms.txt
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/graphql/cancer-gov-gdc.graphql
  title: ''
  type: GraphQL
  url: graphql/cancer-gov-gdc.graphql
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/conformance/cancer-gov-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cancer-gov-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/errors/cancer-gov-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cancer-gov-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/lifecycle/cancer-gov-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cancer-gov-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://api.gdc.cancer.gov/status
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/conventions/cancer-gov-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cancer-gov-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/changelog/cancer-gov-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cancer-gov-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/data-model/cancer-gov-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cancer-gov-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/plans/cancer-gov-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cancer-gov-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/rate-limits/cancer-gov-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cancer-gov-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/overlays/cancer-gov-seer-overlay.yaml
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
overview: 'Cancer.gov publishes 45 APIs on the [APIs.io](https://apis.io/) network, including Diseases API, Interventions API, Terms API, and 42 more. Tagged areas include Cancer, Federal-Government, Healthcare, Research, and Clinical Trials.


  Cancer.gov''s developer surface includes authentication, engineering blog, CLI, changelog, documentation, API reference, signup flow, and 39 more developer resources.'
plans:
- name: Cancer Gov Plans Pricing
  plan_count: 1
  slug: cancer-gov-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Cancer Gov Rate Limits
  slug: cancer-gov-rate-limits
score:
  band: developing
  composite: 53.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 55.0
    catalog_earned_first_party: 20.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 48.6
    developer_ergonomics: 61.3
    discoverability: 59.3
    operational_transparency: 57.9
  previous_composite: 51.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 50.0
      derived: 3
      marker_coverage: 6.7
      total: 45
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
