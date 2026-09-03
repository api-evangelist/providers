---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Bigid Agentic Access
  operation_count: 27
  slug: bigid-agentic-access
  summary_line: 27 operations · 9 acting
api_count: 3
apis:
- baseURL: https://sandbox.bigid.tools/api/v1
  baseurl_source: spec
  description: Authenticate against a BigID deployment using either username/password or a long-lived user token. Exchange a user token for a short-lived system token (JWT) used to authorize subsequent REST API call
  name: BigID Authentication API
  slug: bigid-authentication-api
- baseURL: https://sandbox.bigid.tools/api/v1
  baseurl_source: spec
  description: Programmatically manage data source connections in BigID. List, create, test, and export data sources, and inspect the catalog of available connector templates (e.g. rdb-mysql, s3-v2, snowflake, share
  name: BigID Data Sources API
  slug: bigid-data-sources-api
- baseURL: https://sandbox.bigid.tools/api/v1
  baseurl_source: spec
  description: Configure and execute BigID scans. Create scan profiles to control which data sources are scanned and using which classifier template, then start and monitor scan executions and parent-scan rollups.
  name: BigID Scans API
  slug: bigid-scans-api
- baseURL: https://sandbox.bigid.tools/api/v1
  baseurl_source: spec
  description: Run Data Subject Access Requests (DSARs) and retrieve the resulting reports. Inspect available DSAR profiles and identifier attributes, submit new DSAR scans, poll status, and download short or full r
  name: BigID DSAR API
  slug: bigid-dsar-api
- baseURL: https://sandbox.bigid.tools/api/v1
  baseurl_source: spec
  description: DSPM cases and remediation.
  name: BigID Actionable Insights API
  slug: bigid-actionable-insights-api
- baseURL: https://sandbox.bigid.tools/api/v1
  baseurl_source: spec
  description: Browse catalog objects.
  name: BigID Catalog API
  slug: bigid-catalog-api
- baseURL: https://sandbox.bigid.tools/api/v1
  baseurl_source: spec
  description: Cluster analysis operations.
  name: BigID Clusters API
  slug: bigid-clusters-api
- baseURL: https://sandbox.bigid.tools/api/v1
  baseurl_source: spec
  description: Inspect available connector templates.
  name: BigID Connector Templates API
  slug: bigid-connector-templates-api
- baseURL: https://sandbox.bigid.tools/api/v1
  baseurl_source: spec
  description: Export catalog metadata.
  name: BigID Metadata Export API
  slug: bigid-metadata-export-api
- baseURL: https://sandbox.bigid.tools/api/v1
  baseurl_source: spec
  description: Configure recurring scan profiles.
  name: BigID Scan Profiles API
  slug: bigid-scan-profiles-api
artifact_total: 87
collections:
- collection_type: postman
  name: BigID Authentication Actionable Insights API
  slug: postman-bigid-actionable-insights-api
- collection_type: postman
  name: BigID Actionable Insights Authentication API
  slug: postman-bigid-authentication-api
- collection_type: postman
  name: BigID Authentication Actionable Insights Catalog API
  slug: postman-bigid-catalog-api
- collection_type: postman
  name: BigID Authentication Actionable Insights Clusters API
  slug: postman-bigid-clusters-api
- collection_type: postman
  name: BigID Authentication Actionable Insights Connector Templates API
  slug: postman-bigid-connector-templates-api
- collection_type: postman
  name: BigID Authentication Actionable Insights Data Sources API
  slug: postman-bigid-data-sources-api
- collection_type: postman
  name: BigID Authentication Actionable Insights DSAR API
  slug: postman-bigid-dsar-api
- collection_type: postman
  name: BigID Authentication Actionable Insights Metadata Export API
  slug: postman-bigid-metadata-export-api
- collection_type: postman
  name: BigID Authentication Actionable Insights Scan Profiles API
  slug: postman-bigid-scan-profiles-api
- collection_type: postman
  name: BigID Authentication Actionable Insights Scans API
  slug: postman-bigid-scans-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BigID Authentication Actionable Insights API
  slug: open-bigid-actionable-insights-api
- collection_type: open
  name: BigID Actionable Insights Authentication API
  slug: open-bigid-authentication-api
- collection_type: open
  name: BigID Authentication Actionable Insights Catalog API
  slug: open-bigid-catalog-api
- collection_type: open
  name: BigID Cluster Analysis API
  slug: open-bigid-cluster-analysis-api
- collection_type: open
  name: BigID Authentication Actionable Insights Clusters API
  slug: open-bigid-clusters-api
- collection_type: open
  name: BigID Authentication Actionable Insights Connector Templates API
  slug: open-bigid-connector-templates-api
- collection_type: open
  name: BigID Data Catalog API
  slug: open-bigid-data-catalog-api
- collection_type: open
  name: BigID Data Posture API
  slug: open-bigid-data-posture-api
- collection_type: open
  name: BigID Authentication Actionable Insights Data Sources API
  slug: open-bigid-data-sources-api
- collection_type: open
  name: BigID Authentication Actionable Insights DSAR API
  slug: open-bigid-dsar-api
- collection_type: open
  name: BigID Authentication Actionable Insights Metadata Export API
  slug: open-bigid-metadata-export-api
- collection_type: open
  name: BigID Authentication Actionable Insights Scan Profiles API
  slug: open-bigid-scan-profiles-api
- collection_type: open
  name: BigID Authentication Actionable Insights Scans API
  slug: open-bigid-scans-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/bigid/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bigid-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bigid-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bigid-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bigid-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bigid-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bigid.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.bigid.com/guides/get-started/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.bigid.com/api/bigid-api/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bigid.com/apps/building-a-bigid-app/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bigid.com/connectors/what-is-a-bigid-connector/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bigid.com/llms/llms/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bigexchange
- group: build
  title: ''
  type: SDKs
  url: https://github.com/bigexchange/sdk-javascript
- group: build
  title: ''
  type: SDKs
  url: https://github.com/bigexchange/consent-sdk-ios
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/bigexchange/quickstart-simple-ts
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/bigexchange/quickstart-utility-dspm-ts
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/bigexchange/app-framework-helloworld-app
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/bigexchange/helm-template
- group: start
  title: ''
  type: Portal
  url: https://bigid.com/
- group: company
  title: ''
  type: Blog
  url: https://bigid.com/blog/
- group: other
  title: ''
  type: Hub
  url: https://bigid.com/about/
- group: operate
  title: ''
  type: Contact
  url: https://bigid.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bigid.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bigid.com/privacy-notice/
- group: commercial
  title: ''
  type: Legal
  url: https://bigid.com/cookies/
- group: auth
  title: ''
  type: Compliance
  url: https://bigid.com/sub-processors/
- group: auth
  title: ''
  type: Compliance
  url: https://bigid.com/certifications-and-assessments/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bigid/
- group: design
  title: ''
  type: SpectralRules
  url: rules/bigid-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/bigid-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/bigid-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/bigid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bigid-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bigid-finops.yml
created: '2026-05-25'
description: BigID is a New York City-headquartered data security platform that combines Data Security Posture Management (DSPM), Data Loss Prevention (DLP), access governance, AI security & governance (AISPM), privacy automation, and a unified Data & AI Catalog. Founded in 2016 by Dimitri Sirota and Nimrod Vax, BigID exposes every action available in its UI through a REST API rooted at /api/v1 — covering data sources, scans, catalog, cluster analysis, DSPM cases, and DSARs — plus an App Framework for building custom apps, a connector framework (Java and REST) for new data sources, and an MCP surface for AI agents.
examples:
- key_count: 2
  name: Bigid Create Dsar Report Example
  slug: bigid-create-dsar-report-example
- key_count: 2
  name: Bigid Create Session Example
  slug: bigid-create-session-example
- key_count: 2
  name: Bigid List Data Sources Example
  slug: bigid-list-data-sources-example
- key_count: 2
  name: Bigid List Posture Cases Example
  slug: bigid-list-posture-cases-example
features:
- description: Continuous risk detection across cloud, on-prem, and SaaS data with severity-based remediation workflows.
  name: Data Security Posture Management (DSPM)
- description: ML-enhanced DLP with custom labeling by sensitivity, residency, and risk; integrates with MIP and Google labels.
  name: Data Loss Prevention (DLP)
- description: Identify over-privileged access, enable zero-trust controls, and mitigate insider risk.
  name: Access Governance
- description: Shadow AI detection, AI model inventory, prompt and response governance, TRiSM (Trust, Risk & Security Management for AI).
  name: AI Security & Governance (AISPM)
- description: DSAR fulfillment, retention, deletion, consent, and 190,000+ out-of-the-box retention policies.
  name: Privacy Automation
- description: Unified catalog of structured and unstructured data, AI models, prompts, and agents; federates with third-party catalogs.
  name: Data & AI Catalog
- description: Cloud, SaaS, on-prem, and developer-environment connectors. Java-based or REST-based connector framework for custom sources.
  name: 100+ Data Source Connectors
- description: Patented AI classification across 100+ languages, plus regex, NLP, and customer-built classifiers.
  name: 1000+ Pre-Trained Classifiers
- description: Build custom apps that integrate with BigID via /manifest, /execute, and /ui HTTP endpoints; deploy alongside BigID on Kubernetes.
  name: App Framework
- description: BigID exposes its data governance and connector surface through the Model Context Protocol so AI agents can drive it.
  name: MCP for Agents
finops:
- name: Bigid Finops
  service_category: Security
  slug: bigid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bigid.png
integrations:
- description: Bidirectional integrations with AWS Security Hub, Control Tower, S3, RDS, and more.
  name: AWS
- description: Discover, classify, and govern data inside Snowflake warehouses.
  name: Snowflake
- description: Catalog and protect data in Databricks Lakehouse and Unity Catalog.
  name: Databricks
- description: Stream BigID findings into Splunk for SOC monitoring and SIEM correlation.
  name: Splunk
- description: Combine BigID data context with Wiz cloud-posture findings.
  name: Wiz
- description: Discover and govern PII in Salesforce orgs.
  name: Salesforce
- description: Drive remediation workflows via ServiceNow tickets.
  name: ServiceNow
- description: Federate BigID's catalog with Collibra's governance platform.
  name: Collibra
- description: Sync BigID metadata into Alation's data intelligence platform.
  name: Alation
- description: Federate with Informatica IDMC for data management workflows.
  name: Informatica
- description: Sync classifications and lineage with Atlan.
  name: Atlan
- description: Apply MIP sensitivity labels driven by BigID classifications.
  name: Microsoft Information Protection (MIP)
- description: SOAR playbooks for managing data permissions and scans (via bigexchange/content).
  name: Cortex XSOAR
- description: Cookie consent template for GTM (via bigexchange/gtm-consent-template).
  name: Google Tag Manager
json_schemas:
- name: BigID Actionable Insights Case
  property_count: 8
  slug: bigid-case
- name: BigID Catalog Object
  property_count: 10
  slug: bigid-catalog-object
- name: BigID Data Source
  property_count: 8
  slug: bigid-data-source
jsonld:
- class_count: 0
  name: Bigid Context
  property_count: 6
  slug: bigid-context
layout: provider
modified: '2026-05-25'
name: BigID
nav: Providers
network: true
overview: 'BigID publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Data Sources API, Scans API, and 7 more. Tagged areas include Data Security, DSPM, DLP, Privacy, and AI Security.


  The BigID catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  BigID''s developer surface includes authentication, getting-started guide, API reference, documentation, code examples, developer portal, engineering blog, and 28 more developer resources.'
plans:
- name: Bigid Plans Pricing
  plan_count: 4
  slug: bigid-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Bigid Rate Limits
  slug: bigid-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: BigID API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: bigid-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: BigID API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: bigid-rules
score:
  band: strong
  composite: 55.5
  coverage:
    artifact_dirs: 16
    catalog_gap: 40.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 28.8
    contract_quality: 66.9
    developer_ergonomics: 64.3
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 5.3
  previous_composite: 55.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bigid/refs/heads/main/screenshots/bigid-2026-06-20T173239.png
security:
- kind: authentication
  name: Bigid Authentication
  slug: bigid-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bigid Domain Security
  slug: bigid-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bigid Vulnerability Disclosure
  slug: bigid-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Bigid Trust Center
  slug: bigid-trust-center
  summary_line: PCI DSS, HIPAA, GDPR
slug: bigid
solutions:
- description: DSPM + DLP + access governance in one platform.
  name: Data Security Platform
- description: DSAR, retention, deletion, consent, and regulatory reporting.
  name: Privacy Automation Suite
- description: Shadow AI, model inventory, prompt/response governance, TRiSM.
  name: AI Security & Governance
- description: Unified catalog spanning structured, unstructured, and AI assets.
  name: Data & AI Catalog
tags:
- Data Security
- DSPM
- DLP
- Privacy
- AI Security
- Data Catalog
- DSAR
- Data Discovery
- Compliance
use_cases:
- description: Discover, govern, and secure AI models, training data, prompts, and agent surfaces across the enterprise.
  name: AI Risk Management and TRiSM
- description: Find and remediate exposed PII, PHI, PCI, and other sensitive data in S3, GCS, Azure Storage, Snowflake, and Databricks.
  name: Cloud Data Security
- description: Surface duplicate and stale data to shrink the sensitive-data footprint.
  name: Data Minimization
- description: Operationalize HIPAA, GDPR, CCPA, LGPD, and other privacy regimes with DSAR, retention, and consent automation.
  name: Privacy Compliance
- description: Spot suspicious access to sensitive data based on behavior, role, and policy.
  name: Insider Risk Detection
- description: Determine what sensitive data was implicated in an incident and notify accordingly.
  name: Breach Investigation
- description: Prevent exfiltration of source code and credentials from code repositories and developer environments.
  name: Source Code DLP
website: https://developer.bigid.com/
---
