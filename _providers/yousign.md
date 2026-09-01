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
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 89
  human_in_the_loop: 0
  name: Yousign Agentic Access
  operation_count: 166
  slug: yousign-agentic-access
  summary_line: 166 operations · 89 acting
api_count: 1
apis:
- description: An applicant associated with a Workflow Session.
  name: YouSign Applicant API
  slug: yousign-applicant-api
- description: Person responsible for validating a Signature Request.
  name: YouSign Approver API
  slug: yousign-approver-api
- description: A feature allowing to store and retrieve documents on Arkhineo for some customers migrated from v2
  name: YouSign Archive API
  slug: yousign-archive-api
- description: Set of documents generated once a Signature Request is completed.
  name: YouSign Audit Trail API
  slug: yousign-audit-trail-api
- description: KYC Process of verifying a person’s or company’s banking information via the Sepamail DIAMOND network.
  name: YouSign Bank Account Lookup Verification API
  slug: yousign-bank-account-lookup-verification-api
- description: KYC Process of verifying the identity associated with a bank account document.
  name: YouSign Bank Account Verification API
  slug: yousign-bank-account-verification-api
- description: Retrieve structured and official data about a company.
  name: YouSign Company Verification API
  slug: yousign-company-verification-api
- description: This resource provides tracking of the API usage.
  name: YouSign Consumption API
  slug: yousign-consumption-api
- description: A saved profile containing some information (name, language, email address, etc.) that can be re-used to create a Signer, Approver, or Follower.
  name: YouSign Contact API
  slug: yousign-contact-api
- description: Allows to customize the look and feel of the signature experience.
  name: YouSign Custom Experience API
  slug: yousign-custom-experience-api
- description: A configurable field (list or text) allowing to tag Signature Requests with structured values.
  name: YouSign Custom Property API
  slug: yousign-custom-property-api
- description: Operations that are no longer recommended for use.
  name: YouSign Deprecated API
  slug: yousign-deprecated-api
- description: Analyze a document and extract structured data.
  name: YouSign Document Analysis API
  slug: yousign-document-analysis-api
- description: Document that is attached to the Signature Request.
  name: YouSign Document API
  slug: yousign-document-api
- description: This resource is the digital version of the company stamp.
  name: YouSign Electronic Seal API
  slug: yousign-electronic-seal-api
- description: Set of documents generated once a Electronic Seal is completed.
  name: YouSign Electronic Seal Audit Trail API
  slug: yousign-electronic-seal-audit-trail-api
- description: Document that is attached to the Electronic Seal.
  name: YouSign Electronic Seal Document API
  slug: yousign-electronic-seal-document-api
- description: Set of Image which can be used in Electronic Seal.
  name: YouSign Electronic Seal Image API
  slug: yousign-electronic-seal-image-api
- description: Dynamic content that will appear on a Document.
  name: YouSign Field API
  slug: yousign-field-api
- description: Person who is kept informed about the progress of the signing process without being an Approver or a Signer.
  name: YouSign Follower API
  slug: yousign-follower-api
- description: KYC Process of verifying the identity associated with an identity document.
  name: YouSign Identity Document Verification API
  slug: yousign-identity-document-verification-api
- description: KYC Process of verifying the identity associated with a document.
  name: YouSign Identity Video Verification API
  slug: yousign-identity-video-verification-api
- description: Categorization tag that can be added to a Signature Request.
  name: YouSign Label API
  slug: yousign-label-api
- description: Extra information attached to a Signature Request.
  name: YouSign Metadata API
  slug: yousign-metadata-api
- description: KYC Process of verifying a proof of address document.
  name: YouSign Proof of Address Verification API
  slug: yousign-proof-of-address-verification-api
- description: Process of inviting Signers to sign a Document.
  name: YouSign Signature Request API
  slug: yousign-signature-request-api
- description: Person who will sign a Signature Request.
  name: YouSign Signer API
  slug: yousign-signer-api
- description: Process of asking signers to consent to specific needs during the signature process.
  name: YouSign Signer Consent Request API
  slug: yousign-signer-consent-request-api
- description: Process of asking signers to upload specific documents during the signature process.
  name: YouSign Signer Document Request API
  slug: yousign-signer-document-request-api
- description: Pre-configuration of all elements of a Signature Request, such as Documents, Signers, Approvers, Fields, and settings.
  name: YouSign Template API
  slug: yousign-template-api
- description: A person who can access the Yousign web app of your organization.
  name: YouSign User API
  slug: yousign-user-api
- description: The Invitation of a new User to join the Yousign organization.
  name: YouSign User Invitation API
  slug: yousign-user-invitation-api
- description: Set of documents generated once a Verification is completed.
  name: YouSign Verification Audit Trail API
  slug: yousign-verification-audit-trail-api
- description: Check if individuals appear on international sanctions lists or as politically exposed persons (PEPs).
  name: YouSign Watchlist Verification API
  slug: yousign-watchlist-verification-api
- description: Webhook subscription; enables real-time notifications about events that happen in your Yousign organization.
  name: YouSign Webhook API
  slug: yousign-webhook-api
- description: Instance of a workflow created each time a customer goes through it.
  name: YouSign Workflow Session API
  slug: yousign-workflow-session-api
- description: Structure of a workflow defined by the type of Actions a customer must complete.
  name: YouSign Workflow Template API
  slug: yousign-workflow-template-api
- description: A way to partition your Yousign organization into separate entities.
  name: YouSign Workspace API
  slug: yousign-workspace-api
artifact_total: 86
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Public Api v3 Applicant API
  slug: open-yousign-applicant-api
- collection_type: open
  name: Public Api v3 Applicant Approver API
  slug: open-yousign-approver-api
- collection_type: open
  name: Public Api v3 Applicant Archive API
  slug: open-yousign-archive-api
- collection_type: open
  name: Public Api v3 Applicant Audit Trail API
  slug: open-yousign-audit-trail-api
- collection_type: open
  name: Public Api v3 Applicant Bank Account Lookup Verification API
  slug: open-yousign-bank-account-lookup-verification-api
- collection_type: open
  name: Public Api v3 Applicant Bank Account Verification API
  slug: open-yousign-bank-account-verification-api
- collection_type: open
  name: Public Api v3 Applicant Company Verification API
  slug: open-yousign-company-verification-api
- collection_type: open
  name: Public Api v3 Applicant Consumption API
  slug: open-yousign-consumption-api
- collection_type: open
  name: Public Api v3 Applicant Contact API
  slug: open-yousign-contact-api
- collection_type: open
  name: Public Api v3 Applicant Custom Experience API
  slug: open-yousign-custom-experience-api
- collection_type: open
  name: Public Api v3 Applicant Custom Property API
  slug: open-yousign-custom-property-api
- collection_type: open
  name: Public Api v3 Applicant Deprecated API
  slug: open-yousign-deprecated-api
- collection_type: open
  name: Public Api v3 Applicant Document Analysis API
  slug: open-yousign-document-analysis-api
- collection_type: open
  name: Public Api v3 Applicant Document API
  slug: open-yousign-document-api
- collection_type: open
  name: Public Api v3 Applicant Electronic Seal API
  slug: open-yousign-electronic-seal-api
- collection_type: open
  name: Public Api v3 Applicant Electronic Seal Audit Trail API
  slug: open-yousign-electronic-seal-audit-trail-api
- collection_type: open
  name: Public Api v3 Applicant Electronic Seal Document API
  slug: open-yousign-electronic-seal-document-api
- collection_type: open
  name: Public Api v3 Applicant Electronic Seal Image API
  slug: open-yousign-electronic-seal-image-api
- collection_type: open
  name: Public Api v3 Applicant Field API
  slug: open-yousign-field-api
- collection_type: open
  name: Public Api v3 Applicant Follower API
  slug: open-yousign-follower-api
- collection_type: open
  name: Public Api v3 Applicant Identity Document Verification API
  slug: open-yousign-identity-document-verification-api
- collection_type: open
  name: Public Api v3 Applicant Identity Video Verification API
  slug: open-yousign-identity-video-verification-api
- collection_type: open
  name: Public Api v3 Applicant Label API
  slug: open-yousign-label-api
- collection_type: open
  name: Public Api v3 Applicant Metadata API
  slug: open-yousign-metadata-api
- collection_type: open
  name: Public Api v3 Applicant Proof of Address Verification API
  slug: open-yousign-proof-of-address-verification-api
- collection_type: open
  name: Public Api v3 Applicant Signature Request API
  slug: open-yousign-signature-request-api
- collection_type: open
  name: Public Api v3 Applicant Signer API
  slug: open-yousign-signer-api
- collection_type: open
  name: Public Api v3 Applicant Signer Consent Request API
  slug: open-yousign-signer-consent-request-api
- collection_type: open
  name: Public Api v3 Applicant Signer Document Request API
  slug: open-yousign-signer-document-request-api
- collection_type: open
  name: Public Api v3 Applicant Template API
  slug: open-yousign-template-api
- collection_type: open
  name: Public Api v3 Applicant User API
  slug: open-yousign-user-api
- collection_type: open
  name: Public Api v3 Applicant User Invitation API
  slug: open-yousign-user-invitation-api
- collection_type: open
  name: Public Api v3 Applicant Verification Audit Trail API
  slug: open-yousign-verification-audit-trail-api
- collection_type: open
  name: Public Api v3 Applicant Watchlist Verification API
  slug: open-yousign-watchlist-verification-api
- collection_type: open
  name: Public Api v3 Applicant Webhook API
  slug: open-yousign-webhook-api
- collection_type: open
  name: Public Api v3 Applicant Workflow Session API
  slug: open-yousign-workflow-session-api
- collection_type: open
  name: Public Api v3 Applicant Workflow Template API
  slug: open-yousign-workflow-template-api
- collection_type: open
  name: Public Api v3 Applicant Workspace API
  slug: open-yousign-workspace-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/yousign-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/yousign-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/yousign-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yousign-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/yousign-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://yousign.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.yousign.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Yousign
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yousign
- group: company
  title: ''
  type: Blog
  url: https://yousign.com/blog
- group: company
  title: ''
  type: EngineeringBlog
  url: https://blog.yousign.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://yousign.com/pricing-api
- group: operate
  title: ''
  type: StatusPage
  url: https://yousign.statuspage.io/
- group: other
  title: ''
  type: X
  url: https://twitter.com/Yousignfr
- group: other
  title: ''
  type: Developers
  url: https://yousign.com/developers
- group: commercial
  title: ''
  type: Plans
  url: plans/yousign-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/yousign-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/yousign-finops.yml
created: '2026-06-13'
description: European e-signature platform compliant with eIDAS with a REST API for creating signature requests, managing signers, sending documents, and tracking signing workflows across simple, advanced, and qualified signature levels.
finops:
- name: Yousign Finops
  service_category: ''
  slug: yousign-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yousign.png
jsonld:
- class_count: 29
  name: Yousign Context
  property_count: 24
  slug: yousign-context
layout: provider
modified: '2026-06-13'
name: YouSign
nav: Providers
network: true
overview: 'YouSign publishes 38 APIs on the [APIs.io](https://apis.io/) network, including Applicant API, Approver API, Archive API, and 35 more. Tagged areas include E-Signature, Electronic Signature, eIDAS, Digital Signature, and Document Signing.


  The YouSign catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  YouSign''s developer surface includes authentication, documentation, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Yousign Plans Pricing
  plan_count: 4
  slug: yousign-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 7
  name: Yousign Rate Limits
  slug: yousign-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: YouSign API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: yousign-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.7
  coverage:
    artifact_dirs: 16
    catalog_gap: 28.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 76.2
    developer_ergonomics: 27.4
    discoverability: 63.0
    governance: 25.0
    operational_transparency: 60.5
  previous_composite: 51.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 38
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yousign/refs/heads/main/screenshots/yousign-2026-06-20T201749.png
security:
- kind: authentication
  name: Yousign Authentication
  slug: yousign-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Yousign Domain Security
  slug: yousign-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Yousign Vulnerability Disclosure
  slug: yousign-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: yousign
tags:
- E-Signature
- Electronic Signature
- eIDAS
- Digital Signature
- Document Signing
- Europe
- REST API
- Signature Workflows
website: https://yousign.com
---
