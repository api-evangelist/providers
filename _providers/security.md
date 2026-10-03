---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 31
common:
- group: start
  title: ''
  type: Portal
  url: https://apievangelist.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2026-05-19'
description: An index and topic collection covering API security, identity, access management, secrets management, encryption, and threat protection. API security spans the full lifecycle of an API, from designing strong authentication and authorization, to managing keys, secrets, and certificates, to protecting runtime traffic with WAFs, rate limiting, and bot mitigation, to scanning code and dependencies for vulnerabilities. This collection brings together identity providers like Okta, Auth0, and Keycloak; secrets and key management platforms like HashiCorp Vault and AWS KMS; cloud security and WAF vendors like Cloudflare, Akamai, and Palo Alto Networks; and software supply chain security tools like Snyk, Sigstore, and Sonatype.
examples:
- key_count: 16
  name: Security Oauth Client Example
  slug: security-oauth-client-example
- key_count: 13
  name: Security Secret Example
  slug: security-secret-example
features:
- description: Identity platforms like Okta, Auth0, Keycloak, and Microsoft Entra provide OAuth 2.0, OIDC, SAML, and social login flows so APIs do not have to roll their own authentication.
  name: Authentication and Identity
- description: Tools like OpenFGA, Ory, Amazon Verified Permissions, and SailPoint implement role-based, attribute-based, and relationship-based access control at the API and resource level.
  name: Authorization and Fine-Grained Access
- description: Platforms like HashiCorp Vault, AWS KMS, Azure Key Vault, and 1Password centralize the storage, rotation, and auditing of API keys, tokens, database credentials, and encryption keys.
  name: Secrets and Key Management
- description: Edge security platforms like Cloudflare, Akamai, Amazon WAF, and Fortinet inspect API traffic for OWASP API Top 10 attacks, bot abuse, credential stuffing, and DDoS at the network edge.
  name: API Threat Protection and WAF
- description: Specialized API security tools like 42Crunch, Traceable, and Salt scan OpenAPI specifications and live traffic for misconfigurations, broken authentication, and excessive data exposure.
  name: API Security Posture and Scanning
- description: Tools like Snyk, Sonatype, JFrog Xray, Sigstore, and Trivy scan code, dependencies, containers, and artifacts for vulnerabilities and verify provenance before APIs reach production.
  name: Software Supply Chain Security
- description: Runtime security platforms like Falco, Sysdig, Aqua Security, and StackRox monitor containers and Kubernetes workloads that host APIs for suspicious behavior and policy violations.
  name: Runtime and Workload Security
- description: Certificate authorities and managers like Let's Encrypt, DigiCert, and AWS Private CA issue, rotate, and revoke TLS certificates that secure API endpoints in transit.
  name: Certificate and TLS Management
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: Identity platform providing OAuth 2.0, OIDC, SAML, MFA, and lifecycle management for workforce and customer identities accessing APIs.
  name: Okta
- description: Developer-friendly identity platform (now part of Okta) for adding authentication, social login, and authorization to APIs.
  name: Auth0
- description: Secrets management platform for storing, rotating, and dynamically issuing API tokens, database credentials, certificates, and encryption keys.
  name: HashiCorp Vault
- description: Global edge platform providing WAF, API Shield, bot management, rate limiting, mTLS, and DDoS protection for APIs.
  name: Cloudflare
- description: Developer-first security platform that scans code, dependencies, containers, and IaC for vulnerabilities affecting API services.
  name: Snyk
- description: Open-source identity and access management server implementing OAuth 2.0, OIDC, and SAML for protecting APIs and applications.
  name: Keycloak
- description: Open-source project for signing, verifying, and proving the provenance of software artifacts used in API supply chains.
  name: Sigstore
- description: API security platform that audits OpenAPI definitions, scans live APIs, and enforces security policies at the gateway.
  name: 42Crunch
json_schemas:
- name: OAuthClient
  property_count: 16
  slug: security-oauth-client
- name: Secret
  property_count: 13
  slug: security-secret
json_structures:
- name: Security Oauth Client Structure
  property_count: 16
  slug: security-oauth-client-structure
- name: Security Secret Structure
  property_count: 13
  slug: security-secret-structure
jsonld:
- class_count: 6
  name: Security Context
  property_count: 27
  slug: security-context
layout: provider
modified: '2026-05-19'
name: Security
nav: Providers
network: true
overview: 'Security is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include API Security, Identity and Access Management, Authentication, Secrets Management, and Threat Protection.


  The Security catalog on APIs.io includes 1 JSON-LD context.


  Security''s developer surface includes developer portal and 1 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: security
tags:
- API Security
- Identity and Access Management
- Authentication
- Secrets Management
- Threat Protection
use_cases:
- description: Use an identity provider like Okta, Auth0, or Keycloak to issue access tokens and ID tokens that API gateways and services validate on every request.
  name: OAuth 2.0 and OIDC for API Access
- description: Replace hard-coded credentials with short-lived secrets fetched from HashiCorp Vault or AWS Secrets Manager so each service authenticates with its own dynamically issued identity.
  name: Centralized Secrets for Microservices
- description: Place a WAF like Cloudflare or Akamai in front of public APIs to block OWASP API Top 10 attacks, credential stuffing, scraping bots, and volumetric DDoS before they reach origin.
  name: WAF and Bot Mitigation in Front of APIs
- description: Integrate API security scanners like 42Crunch and dependency scanners like Snyk into CI/CD pipelines so vulnerabilities are caught before APIs ship.
  name: API Security Testing in CI/CD
- description: Use CyberArk, BeyondTrust, or 1Password to broker, monitor, and rotate access to administrative APIs and infrastructure credentials.
  name: Privileged Access Management
- description: Issue cryptographic workload identities with SPIFFE/SPIRE so services authenticate to APIs using verifiable identities instead of static API keys.
  name: Zero Trust and Workload Identity
- description: Continuously scan APIs, hosts, containers, and cloud accounts with Qualys, Rapid7, CrowdStrike, or Sysdig to detect exposed endpoints and misconfigurations.
  name: Vulnerability and Posture Management
- description: Use Sigstore, Sonatype, and JFrog Xray to sign, verify, and attest the provenance of API server images and their dependencies.
  name: Signed Artifacts and Supply Chain Attestation
website: https://apievangelist.com
---
