---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Amazon Lake Formation Agentic Access
  operation_count: 7
  slug: amazon-lake-formation-agentic-access
  summary_line: 7 operations · 4 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Data lake resource management
  name: Amazon Lake Formation Resources API
  slug: amazon-lake-formation-resources-api
arazzos:
- description: Enumerate registered data lake locations and list the permissions on a selected resource.
  name: Amazon Lake Formation Audit Resource Permissions
  slug: amazon-lake-formation-audit-resource-permissions-workflow
- description: Confirm a registered data lake location exists, deregister it, and verify removal.
  name: Amazon Lake Formation Deregister Resource Lifecycle
  slug: amazon-lake-formation-deregister-resource-workflow
- description: Grant a destination principal the same permissions and then revoke them from the source principal.
  name: Amazon Lake Formation Migrate Principal Permissions
  slug: amazon-lake-formation-migrate-principal-permissions-workflow
- description: Register an Amazon S3 location as a data lake resource and grant a principal access to it.
  name: Amazon Lake Formation Register Resource and Grant Permissions
  slug: amazon-lake-formation-register-and-grant-workflow
- description: Swap the IAM data access role on a registered data lake location by deregistering and re-registering it.
  name: Amazon Lake Formation Rotate Resource Data Access Role
  slug: amazon-lake-formation-reregister-resource-role-workflow
- description: Revoke a principal's permissions on a resource and verify they were removed.
  name: Amazon Lake Formation Revoke Permissions and Verify
  slug: amazon-lake-formation-revoke-and-verify-workflow
artifact_total: 36
collections:
- collection_type: postman
  name: Amazon Lake Formation API
  slug: postman-amazon-lake-formation
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Lake Formation Resources API
  slug: open-amazon-lake-formation-resources-api
- collection_type: open
  name: Amazon Lake Formation API
  slug: open-amazon-lake-formation
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-lake-formation-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-lake-formation-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-lake-formation-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-lake-formation-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-lake-formation-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-lake-formation/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-lake-formation-audit-resource-permissions-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-lake-formation-deregister-resource-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-lake-formation-migrate-principal-permissions-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-lake-formation-register-and-grant-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-lake-formation-reregister-resource-role-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-lake-formation-revoke-and-verify-workflow.yml
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/big-data/category/analytics/aws-lake-formation/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/lakeformation/home
- group: build
  title: ''
  type: CLI
  url: https://docs.aws.amazon.com/cli/latest/reference/lakeformation/
- group: build
  title: ''
  type: SDKs
  url: https://aws.amazon.com/tools/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/lake-formation/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/lake-formation/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/lake-formation/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/lake-formation/getting-started/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/lake-formation/faqs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-lake-formation-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-lake-formation-vocabulary.yaml
created: '2024-01-15'
description: AWS Lake Formation is a service that makes it easy to set up a secure data lake in days, providing centralized governance and security for data stored in Amazon S3 and other AWS data stores with fine-grained access control.
examples:
- key_count: 3
  name: Amazon Lake Formation Permission Example
  slug: amazon-lake-formation-permission-example
- key_count: 3
  name: Amazon Lake Formation Resource Example
  slug: amazon-lake-formation-resource-example
features:
- description: Grant table, column, row, and cell-level permissions to data in your data lake.
  name: Fine-Grained Access Control
- description: Centrally define and manage security, governance, and auditing policies across the data lake.
  name: Centralized Governance
- description: Integrates with AWS Glue Data Catalog to discover, catalog, and share metadata.
  name: Data Catalog Integration
- description: Securely share data across AWS accounts without copying it.
  name: Cross-Account Data Sharing
- description: ACID transactions and automatic compaction for governed tables stored in S3.
  name: Governed Tables
finops:
- name: Amazon Lake Formation Finops
  service_category: API
  slug: amazon-lake-formation-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Permission
  property_count: 3
  slug: amazon-lake-formation-permission
- name: DataLakeResource
  property_count: 3
  slug: amazon-lake-formation-resource
json_structures:
- name: Amazon Lake Formation Permission Structure
  property_count: 3
  slug: amazon-lake-formation-permission-structure
- name: Amazon Lake Formation Resource Structure
  property_count: 3
  slug: amazon-lake-formation-resource-structure
jsonld:
- class_count: 2
  name: Amazon Lake Formation Context
  property_count: 7
  slug: amazon-lake-formation-context
layout: provider
modified: '2026-05-19'
name: Amazon Lake Formation
nav: Providers
network: true
overview: 'Amazon Lake Formation publishes 1 API on the [APIs.io](https://apis.io/) network: Resources API. Tagged areas include Access Control, Analytics, Data Governance, Data Lake, and S3.


  The Amazon Lake Formation catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Lake Formation''s developer surface includes authentication, engineering blog, support, developer console, CLI, developer portal, documentation, and 23 more developer resources.'
plans:
- name: Amazon Lake Formation Plans Pricing
  plan_count: 3
  slug: amazon-lake-formation-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Amazon Lake Formation Rate Limits
  slug: amazon-lake-formation-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: Amazon Lake Formation API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: amazon-lake-formation-jsonschema-spectral-rules
- effective_rule_count: 63
  extends:
  - spectral:oas
  name: Amazon Lake Formation API Rules
  rule_count: 22
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 13
  slug: amazon-lake-formation-spectral-rules
score:
  band: strong
  composite: 60.8
  coverage:
    artifact_dirs: 18
    catalog_gap: 44.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 28.8
    contract_quality: 67.3
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 60.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-lake-formation/refs/heads/main/screenshots/amazon-lake-formation-2026-06-20T171721.png
security:
- kind: authentication
  name: Amazon Lake Formation Authentication
  slug: amazon-lake-formation-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Lake Formation Domain Security
  slug: amazon-lake-formation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Lake Formation Vulnerability Disclosure
  slug: amazon-lake-formation-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Lake Formation Trust Center
  slug: amazon-lake-formation-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-lake-formation
tags:
- Access Control
- Analytics
- Data Governance
- Data Lake
- S3
use_cases:
- description: Implement fine-grained access control for data stored in S3 with row and column-level security.
  name: Data Lake Security
- description: Enable business users to discover and access approved data without manual provisioning.
  name: Self-Service Analytics
- description: Share data lake resources across AWS accounts and organizations.
  name: Cross-Account Data Sharing
website: https://aws.amazon.com/lake-formation/
---
