---
access_model:
  confidence: high
  label: Bundled with platform licence · System-account request
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Oracle Health Data Intelligence Agentic Access
  operation_count: 2
  slug: oracle-health-data-intelligence-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: 'Oracle Health Data Intelligence is a comprehensive platform that leverages advanced analytics and artificial intelligence to collect and analyze health data from various sources, including electronic '
  name: Oracle Health Data Intelligence
  slug: oracle-health-data-intelligence
- baseURL: https://cernerdemo.api.us-1.healtheintent.com/allergy/v1
  baseurl_source: declared
  description: 'The Populations API from Oracle Health Data Intelligence — population-scoped read access to a patient''s aggregated allergy record within the longitudinal patient record. Two operations, listAllergies '
  name: Oracle Health Data Intelligence Populations API
  slug: oracle-health-data-intelligence-populations-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Oracle Health Data Intelligence - Allergy Populations API
  slug: open-oracle-health-data-intelligence-populations-api
- collection_type: open
  name: Oracle Health Data Intelligence - Allergy API
  slug: open-oracle-health-data-intelligence
common:
- group: company
  title: ''
  type: Website
  url: https://www.oracle.com/health/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oracle-health-data-intelligence-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oracle-health-data-intelligence-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oracle-health-data-intelligence-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.healtheintent.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.healtheintent.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.healtheintent.com/api/v1/allergy/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.healtheintent.com/#getting-started
- group: operate
  title: ''
  type: Support
  url: https://community.oracle.com/oraclehealth/group/1423-ignite-apis-community
- group: start
  title: ''
  type: Login
  url: https://cernercentral.com/system-accounts/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.oracle.com/corporate/cloud-compliance/
- group: auth
  title: ''
  type: TrustCenter
  url: security/oracle-health-data-intelligence-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/oracle-health-data-intelligence-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/oracle-health-data-intelligence-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/oracle-health-data-intelligence-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/oracle-health-data-intelligence-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/oracle-health-data-intelligence-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/oracle-health-data-intelligence-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/oracle-health-data-intelligence-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/oracle-health-data-intelligence-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/oracle-health-data-intelligence-packages.yml
- group: design
  title: ''
  type: Components
  url: components/oracle-health-data-intelligence-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/oracle-health-data-intelligence-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/oracle-health-data-intelligence-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/oracle-health-data-intelligence-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/oracle-health-data-intelligence-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/oracle-health-data-intelligence-finops.yml
created: '2025-01-07'
description: 'Oracle Health Data Intelligence, formerly Cerner HealtheIntent, is a tenant-scoped population health platform that aggregates data from electronic health records, claims, genomic sources and patient-generated data into a single longitudinal record per patient, then computes intelligence over it — registries, risk scores, hierarchical condition categories, quality measures and care plans. Its public developer portal documents roughly sixty REST APIs spanning the longitudinal record, data ingestion, analytics and syndication, consumer engagement and clinical intelligence. Access is business-to-business and customer-scoped: an Oracle system account is requested through the Cerner Central portal and granted per-API authorization in the Health Data Intelligence Console, authenticating with a bearer token or two-legged OAuth 1.0a. Oracle publishes no machine-readable contract, no SDKs and, by a documented and reasoned decision, no FHIR APIs for this platform.'
finops:
- name: Oracle Health Data Intelligence Finops
  service_category: API
  slug: oracle-health-data-intelligence-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oracle-health-data-intelligence.png
layout: provider
modified: '2026-08-27'
name: Oracle Health Data Intelligence
nav: Providers
network: true
overview: 'Oracle Health Data Intelligence publishes 1 API on the [APIs.io](https://apis.io/) network: Populations API. Tagged areas include Genomic, Health Records, Healthcare, Population Health, and Longitudinal Record.


  Oracle Health Data Intelligence''s developer surface includes authentication, documentation, API reference, getting-started guide, support, sandbox, and 25 more developer resources.'
plans:
- name: Oracle Health Data Intelligence Plans Pricing
  plan_count: 0
  slug: oracle-health-data-intelligence-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Oracle Health Data Intelligence Rate Limits
  slug: oracle-health-data-intelligence-rate-limits
score:
  band: developing
  composite: 51.5
  coverage:
    artifact_dirs: 23
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 18.2
    contract_quality: 53.1
    developer_ergonomics: 55.4
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oracle-health-data-intelligence/refs/heads/main/screenshots/oracle-health-data-intelligence-2026-06-20T191145.png
security:
- kind: authentication
  name: Oracle Health Data Intelligence Authentication
  slug: oracle-health-data-intelligence-authentication
  summary_line: http/oauth1 · 2 schemes
- kind: domain-security
  name: Oracle Health Data Intelligence Domain Security
  slug: oracle-health-data-intelligence-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Oracle Health Data Intelligence Vulnerability Disclosure
  slug: oracle-health-data-intelligence-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Oracle Health Data Intelligence Trust Center
  slug: oracle-health-data-intelligence-trust-center
  summary_line: HIPAA, HITRUST CSF, SOC 2, ISO/IEC 27001, FedRAMP, PCI DSS
slug: oracle-health-data-intelligence
tags:
- Genomic
- Health Records
- Healthcare
- Population Health
- Longitudinal Record
- Interoperability
- Clinical Data
- Analytics
website: https://www.oracle.com/health/
---
