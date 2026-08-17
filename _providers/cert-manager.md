---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 6
apis:
- description: The cert-manager API extends the Kubernetes API with custom resources including Certificate, Issuer, ClusterIssuer, CertificateRequest, and Order. These resources allow declarative management of TLS c
  name: cert-manager Kubernetes API
  slug: cert-manager-api
- description: cmctl is the command-line tool for managing cert-manager resources. It provides commands for checking certificate status, manually triggering renewals, approving or denying certificate requests, and c
  name: cert-manager CLI (cmctl)
  slug: cmctl-cli
- description: trust-manager is a cert-manager companion project for managing TLS trust bundles in Kubernetes and OpenShift clusters. It distributes CA bundles via a Bundle custom resource to namespaces and workload
  name: trust-manager
  slug: trust-manager
- description: 'approver-policy is a cert-manager policy plugin that automatically approves or denies CertificateRequest resources based on defined CertificateRequestPolicy custom resources. It provides fine-grained '
  name: cert-manager approver-policy
  slug: approver-policy
- description: csi-driver is a Kubernetes Container Storage Interface plugin that works alongside cert-manager to seamlessly request and mount certificate key pairs as ephemeral volumes directly into pods. It enable
  name: cert-manager csi-driver
  slug: csi-driver
- description: csi-driver-spiffe is a Kubernetes CSI plugin that works alongside cert-manager to transparently deliver SPIFFE SVIDs as X.509 certificate key pairs to mounted pods using ephemeral volumes. It allows a
  name: cert-manager csi-driver-spiffe
  slug: csi-driver-spiffe
artifact_total: 14
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/cert-manager/cert-manager/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/cert-manager/cert-manager/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/cert-manager/cert-manager/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/cert-manager/cert-manager/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/cert-manager/cert-manager/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cert-manager-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cert-manager.io
- group: docs
  title: ''
  type: Documentation
  url: https://cert-manager.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://cert-manager.io/docs/getting-started/
- group: docs
  title: ''
  type: Reference
  url: https://cert-manager.io/docs/reference/
- group: operate
  title: ''
  type: Community
  url: https://cert-manager.io/docs/contributing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cert-manager
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/cert-manager/cert-manager
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/cert-manager/cert-manager/releases
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cert-manager-certificate-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cert-manager-issuer-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cert-manager-context.jsonld
created: '2026-03-16'
description: cert-manager is a powerful and extensible X.509 certificate controller for Kubernetes and OpenShift workloads. It obtains certificates from a variety of issuers, including Let's Encrypt, HashiCorp Vault, and Venafi, and ensures certificates are valid and up-to-date, attempting to renew them before expiry. It supports certificate issuance for Ingress, Gateway API, and arbitrary workloads via Certificate resources.
finops:
- name: Cert Manager Finops
  service_category: API
  slug: cert-manager-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cert-manager.png
json_schemas:
- name: cert-manager Certificate
  property_count: 5
  slug: cert-manager-certificate
- name: cert-manager Issuer and ClusterIssuer
  property_count: 5
  slug: cert-manager-issuer
jsonld:
- class_count: 0
  name: Cert Manager Context
  property_count: 12
  slug: cert-manager-context
layout: provider
modified: '2026-04-23'
name: Cert-Manager
nav: Providers
network: true
overview: 'Cert-Manager publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Certificates, Cloud Native, Graduated, Kubernetes, and Security.


  The Cert-Manager catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cert-Manager''s developer surface includes documentation, getting-started guide, changelog, and 14 more developer resources.'
plans:
- name: Cert Manager Plans Pricing
  plan_count: 3
  slug: cert-manager-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Cert Manager Rate Limits
  slug: cert-manager-rate-limits
rules:
- name: Cert-Manager API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: cert-manager-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.8
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 29.0
    developer_ergonomics: 30.4
    discoverability: 72.2
    governance: 58.3
    operational_transparency: 39.5
  previous_composite: 35.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cert-manager/refs/heads/main/screenshots/cert-manager-2026-06-20T174140.png
security:
- kind: domain-security
  name: Cert Manager Domain Security
  slug: cert-manager-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cert-manager
tags:
- Certificates
- Cloud Native
- Graduated
- Kubernetes
- Security
- TLS
website: https://cert-manager.io
---
