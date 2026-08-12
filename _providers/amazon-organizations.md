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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Amazon Organizations Agentic Access
  operation_count: 1
  slug: amazon-organizations-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Operations for creating and managing organizations
  name: Amazon Organizations Organizations API
  slug: amazon-organizations-organizations-api
arazzos:
- description: Create an organization with a caller-chosen feature set and branch on the result.
  name: Amazon Organizations Bootstrap Organization By Feature Set
  slug: amazon-organizations-bootstrap-organization-by-feature-set-workflow
- description: Create an organization and capture the management account identity from the response.
  name: Amazon Organizations Capture Management Account Identity
  slug: amazon-organizations-capture-management-account-identity-workflow
- description: Create a new AWS organization with the ALL feature set enabled.
  name: Amazon Organizations Create Organization With All Features
  slug: amazon-organizations-create-organization-all-features-workflow
- description: Create an AWS organization limited to the consolidated billing feature set.
  name: Amazon Organizations Create Consolidated Billing Organization
  slug: amazon-organizations-create-organization-consolidated-billing-workflow
- description: Create an organization and surface its organization and management account ARNs.
  name: Amazon Organizations Record Organization ARNs
  slug: amazon-organizations-record-organization-arns-workflow
- description: Create an organization and assert that it came back with the requested feature set.
  name: Amazon Organizations Verify Organization Feature Set
  slug: amazon-organizations-verify-organization-feature-set-workflow
artifact_total: 36
collections:
- collection_type: postman
  name: Amazon Organizations AWS Organizations API
  slug: postman-amazon-organizations
- collection_type: open
  name: Amazon Organizations AWS Organizations API
  slug: open-amazon-organizations
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-organizations-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-organizations-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-organizations-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-organizations-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-organizations-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-organizations/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-organizations-bootstrap-organization-by-feature-set-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-organizations-capture-management-account-identity-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-organizations-create-organization-all-features-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-organizations-create-organization-consolidated-billing-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-organizations-record-organization-arns-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-organizations-verify-organization-feature-set-workflow.yml
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/security/tag/aws-organizations/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/organizations/
- group: docs
  title: ''
  type: CLI Reference
  url: https://docs.aws.amazon.com/cli/latest/reference/organizations/
- group: build
  title: ''
  type: SDKs
  url: https://aws.amazon.com/tools/
- group: operate
  title: ''
  type: Service Status
  url: https://status.aws.amazon.com/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/organizations/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/organizations/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/organizations/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/organizations/getting-started/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/organizations/faqs/
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
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-organizations
- group: build
  title: ''
  type: Code Examples
  url: https://docs.aws.amazon.com/code-library/latest/ug/organizations_code_examples.html
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-organizations-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-organizations-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-organizations-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-organizations-openapi-context.jsonld
- group: docs
  title: Amazon Organizations
  type: JSONSchema
  url: json-schema/amazon-organizations-schema.json
- group: docs
  title: Openapi Account
  type: JSONSchema
  url: json-schema/openapi-account-schema.json
- group: docs
  title: Openapi Organization
  type: JSONSchema
  url: json-schema/openapi-organization-schema.json
- group: docs
  title: Openapi Organizational Unit
  type: JSONSchema
  url: json-schema/openapi-organizational-unit-schema.json
- group: docs
  title: Openapi Policy
  type: JSONSchema
  url: json-schema/openapi-policy-schema.json
created: '2024-01-15'
description: AWS Organizations is an account management service that enables you to consolidate multiple AWS accounts into an organization that you create and centrally manage.
examples:
- key_count: 11
  name: Amazon Organizations Example
  slug: amazon-organizations-example
- key_count: 7
  name: Openapi Account Example
  slug: openapi-account-example
- key_count: 6
  name: Openapi Organization Example
  slug: openapi-organization-example
- key_count: 3
  name: Openapi Organizational Unit Example
  slug: openapi-organizational-unit-example
- key_count: 2
  name: Openapi Policy Example
  slug: openapi-policy-example
finops:
- name: Amazon Organizations Finops
  service_category: API
  slug: amazon-organizations-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: AWS Organizations Definition
  property_count: 11
  slug: amazon-organizations
- name: Account
  property_count: 7
  slug: openapi-account
- name: Organization
  property_count: 6
  slug: openapi-organization
- name: OrganizationalUnit
  property_count: 3
  slug: openapi-organizational-unit
- name: Policy
  property_count: 2
  slug: openapi-policy
json_structures:
- name: Amazon Organizations Structure
  property_count: 11
  slug: amazon-organizations-structure
- name: Openapi Account Structure
  property_count: 7
  slug: openapi-account-structure
- name: Openapi Organization Structure
  property_count: 6
  slug: openapi-organization-structure
- name: Openapi Organizational Unit Structure
  property_count: 3
  slug: openapi-organizational-unit-structure
- name: Openapi Policy Structure
  property_count: 2
  slug: openapi-policy-structure
jsonld:
- class_count: 0
  name: Amazon Organizations Context
  property_count: 5
  slug: amazon-organizations-context
- class_count: 4
  name: Amazon Organizations Openapi Context
  property_count: 14
  slug: amazon-organizations-openapi-context
layout: provider
modified: '2026-05-19'
name: Amazon Organizations
nav: Providers
network: true
overview: 'Amazon Organizations publishes 1 API on the [APIs.io](https://apis.io/) network: Organizations API. Tagged areas include Account Management, Consolidated Billing, Governance, Multi-Account, and Organizations.


  The Amazon Organizations catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Amazon Organizations'' developer surface includes authentication, engineering blog, support, developer console, documentation, pricing, getting-started guide, and 32 more developer resources.'
plans:
- name: Amazon Organizations Plans Pricing
  plan_count: 3
  slug: amazon-organizations-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Amazon Organizations Rate Limits
  slug: amazon-organizations-rate-limits
rules:
- name: Amazon Organizations API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: amazon-organizations-jsonschema-spectral-rules
- name: Amazon Organizations API Rules
  rule_count: 25
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 14
  slug: amazon-organizations-spectral-rules
score:
  band: strong
  composite: 61.0
  delta: -5.9
  facets:
    commercial_clarity: 76.3
    contract_quality: 73.1
    developer_ergonomics: 54.3
    discoverability: 66.7
    governance: 68.8
    operational_transparency: 13.2
  previous_composite: 66.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-organizations/refs/heads/main/screenshots/amazon-organizations-2026-06-20T171753.png
security:
- kind: authentication
  name: Amazon Organizations Authentication
  slug: amazon-organizations-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Organizations Domain Security
  slug: amazon-organizations-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Organizations Vulnerability Disclosure
  slug: amazon-organizations-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Organizations Trust Center
  slug: amazon-organizations-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-organizations
tags:
- Account Management
- Consolidated Billing
- Governance
- Multi-Account
- Organizations
- Policies
website: https://aws.amazon.com/organizations/
---
