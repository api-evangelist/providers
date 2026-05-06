---
aid: zero-trust-architecture
name: Zero Trust Architecture
description: Zero Trust Architecture (ZTA) is a security framework defined by NIST SP 800-207 that requires all users and devices to be authenticated, authorized, and continuously validated before being granted access to applications and data, regardless of whether they are inside or outside the network perimeter. The architecture is built on the principle of "never trust, always verify," replacing implicit trust with explicit verification for every access request. ZTA leverages APIs, identity providers, policy engines, and continuous monitoring to enforce least-privilege access across enterprise resources.
type: Index
url: https://www.nist.gov/publications/zero-trust-architecture
tags:
  - Access Control
  - Authentication
  - Authorization
  - Cybersecurity
  - Identity Management
  - Least Privilege
  - Network Security
  - NIST
  - Security
  - Zero Trust
created: '2025'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: zero-trust-architecture:nist-sp-800-207
    name: NIST SP 800-207 Zero Trust Architecture
    description: NIST Special Publication 800-207 defines zero trust architecture (ZTA) and provides a roadmap for organizations migrating to ZTA. It describes seven ZTA tenets, three logical components (Policy Decision Point, Policy Enforcement Point, Policy Administration Point), three approaches to ZTA deployment, and guidance on threat models and use cases. Published August 2020.
    humanURL: https://csrc.nist.gov/pubs/sp/800/207/final
    tags:
      - NIST
      - Security Framework
      - Zero Trust
    properties:
      - type: Documentation
        url: https://csrc.nist.gov/pubs/sp/800/207/final
      - type: Documentation
        url: https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-207.pdf
  - aid: zero-trust-architecture:nist-sp-800-207a
    name: NIST SP 800-207A ZTA for Cloud-Native Applications
    description: NIST SP 800-207A extends the original ZTA guidance to cover cloud-native applications in multi-cloud environments. It addresses service mesh architectures, workload identity, microsegmentation, and API-centric access control patterns for containerized workloads.
    humanURL: https://csrc.nist.gov/pubs/sp/800/207/a/final
    tags:
      - Cloud Security
      - Kubernetes
      - NIST
      - Zero Trust
    properties:
      - type: Documentation
        url: https://csrc.nist.gov/pubs/sp/800/207/a/final
      - type: Documentation
        url: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207A.pdf
  - aid: zero-trust-architecture:spiffe
    name: SPIFFE - Secure Production Identity Framework for Everyone
    description: SPIFFE is a CNCF-graduated open standard for workload identity in dynamic environments. It provides a framework for workloads to authenticate to each other using short-lived cryptographic SVIDs (SPIFFE Verifiable Identity Documents) without static secrets, forming a foundational element of API-centric Zero Trust implementations.
    humanURL: https://spiffe.io/
    tags:
      - CNCF
      - Identity
      - Open Source
      - Standards
      - Workload Identity
      - Zero Trust
    properties:
      - type: Documentation
        url: https://spiffe.io/docs/latest/
      - type: GitHubOrganization
        url: https://github.com/spiffe
  - aid: zero-trust-architecture:spire
    name: SPIRE - SPIFFE Runtime Environment
    description: SPIRE is the reference implementation of SPIFFE, a CNCF-graduated production-ready toolchain for establishing trust between workloads. It issues SVIDs to workloads and exposes the SPIFFE Workload API for identity attestation across Kubernetes, VMs, cloud instances, and bare metal environments.
    humanURL: https://spiffe.io/docs/latest/spire-about/spire-concepts/
    tags:
      - CNCF
      - Identity
      - Open Source
      - Runtime
      - Zero Trust
    properties:
      - type: Documentation
        url: https://spiffe.io/docs/latest/spire-about/
      - type: GitHubOrganization
        url: https://github.com/spiffe/spire
  - aid: zero-trust-architecture:open-policy-agent
    name: Open Policy Agent (OPA)
    description: Open Policy Agent is a CNCF-graduated open source general-purpose policy engine that enables unified, context-aware policy enforcement across APIs, microservices, Kubernetes, and CI/CD pipelines. In Zero Trust implementations, OPA serves as the Policy Decision Point (PDP) evaluating access requests against defined policies written in the Rego language.
    humanURL: https://www.openpolicyagent.org/
    tags:
      - Authorization
      - CNCF
      - Open Source
      - Policy Engine
      - Zero Trust
    properties:
      - type: Documentation
        url: https://www.openpolicyagent.org/docs/latest/
      - type: GitHubOrganization
        url: https://github.com/open-policy-agent
common:
  - type: Portal
    title: NIST Zero Trust Architecture
    url: https://www.nist.gov/publications/zero-trust-architecture
    description: Official NIST page for Zero Trust Architecture publications and resources.
  - type: Documentation
    title: NIST SP 800-207 PDF
    url: https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-207.pdf
    description: Downloadable PDF of NIST Special Publication 800-207 Zero Trust Architecture.
  - type: Documentation
    title: NIST SP 800-207A PDF
    url: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207A.pdf
    description: NIST SP 800-207A covering ZTA for cloud-native applications in multi-cloud environments.
  - type: Compliance
    title: CISA Zero Trust Maturity Model
    url: https://www.cisa.gov/zero-trust-maturity-model
    description: CISA's Zero Trust Maturity Model providing a roadmap across five pillars.
  - type: Compliance
    title: NSA Zero Trust Guidance
    url: https://www.nsa.gov/Press-Room/News-Highlights/Article/Article/2899282/nsa-releases-guidance-on-zero-trust-security-model/
    description: NSA guidance on Zero Trust Security Model for network and environment pillar.
  - type: Compliance
    title: DoD Zero Trust Reference Architecture
    url: https://dodcio.defense.gov/Portals/0/Documents/Library/ZT-Reference-Architecture.pdf
    description: Department of Defense Zero Trust Reference Architecture document.
  - type: Portal
    title: SPIFFE Project
    url: https://spiffe.io/
    description: Official site for SPIFFE workload identity standard and SPIRE runtime.
  - type: Portal
    title: Open Policy Agent
    url: https://www.openpolicyagent.org/
    description: Official site for Open Policy Agent (OPA), the CNCF policy engine used as PDP in ZTA.
  - type: GitHubOrganization
    title: SPIFFE GitHub
    url: https://github.com/spiffe
    description: SPIFFE and SPIRE open source repositories on GitHub.
  - type: GitHubOrganization
    title: Open Policy Agent GitHub
    url: https://github.com/open-policy-agent
    description: Open Policy Agent (OPA) GitHub organization.
  - type: JSONSchema
    title: Zero Trust Policy Schema
    url: json-schema/zero-trust-architecture-policy-schema.json
  - type: JSONSchema
    title: Zero Trust Identity Schema
    url: json-schema/zero-trust-architecture-identity-schema.json
  - type: JSONSchema
    title: Zero Trust Resource Schema
    url: json-schema/zero-trust-architecture-resource-schema.json
  - type: JSONLD
    title: Zero Trust Architecture JSON-LD Context
    url: json-ld/zero-trust-architecture-context.jsonld
  - type: JSONStructure
    title: Zero Trust Policy Structure
    url: json-structure/zero-trust-architecture-policy-structure.json
  - type: JSONStructure
    title: Zero Trust Identity Structure
    url: json-structure/zero-trust-architecture-identity-structure.json
  - type: Resources
    title: Zero Trust Architecture Vocabulary
    url: vocabulary/zero-trust-architecture-vocabulary.yaml
  - type: CodeExamples
    title: Zero Trust Policy Example
    url: examples/zero-trust-architecture-policy-example.json
  - type: CodeExamples
    title: Zero Trust Identity Example
    url: examples/zero-trust-architecture-identity-example.json
  - type: Features
    data:
      - name: Identity Verification
        description: Every access request requires verification of user and device identity regardless of network location.
      - name: Least Privilege Access
        description: Access is granted with minimum required permissions on a per-session basis.
      - name: Microsegmentation
        description: Networks are divided into small zones to limit lateral movement after breach.
      - name: Continuous Monitoring
        description: All network traffic, user behavior, and device health are continuously monitored and analyzed.
      - name: Policy Decision Point
        description: Centralized policy engine evaluates access requests against defined policies.
      - name: Policy Enforcement Point
        description: Gateway or proxy that enforces access decisions made by the policy engine.
      - name: Workload Identity
        description: Cryptographic identity for workloads and services replacing static credentials.
      - name: Device Health Attestation
        description: Device posture and compliance are verified before granting access.
      - name: Implicit Trust Elimination
        description: No user, device, or network is trusted implicitly, even inside the corporate perimeter.
      - name: Multi-Factor Authentication
        description: Strong MFA is required as part of identity verification for all access.
  - type: UseCases
    data:
      - name: Remote Workforce Security
        description: Providing secure access to enterprise resources for remote employees without VPN.
      - name: Cloud Application Access
        description: Controlling access to multi-cloud and SaaS applications with consistent policies.
      - name: API Security
        description: Enforcing zero trust principles at API gateways with per-request authentication and authorization.
      - name: Kubernetes Workload Identity
        description: Using SPIFFE/SPIRE to assign cryptographic identities to Kubernetes pods.
      - name: Supply Chain Security
        description: Verifying identity and integrity of software components and build pipelines.
      - name: Government Compliance
        description: Meeting CISA Zero Trust Maturity Model requirements for federal agencies.
      - name: Insider Threat Mitigation
        description: Limiting damage from insider threats through continuous monitoring and least privilege.
      - name: Multi-Cloud Security
        description: Applying consistent zero trust policies across AWS, Azure, GCP, and private clouds.
  - type: Integrations
    data:
      - name: SPIFFE/SPIRE
        description: Workload identity standard providing SVIDs for mutual TLS authentication.
      - name: Open Policy Agent
        description: Policy engine serving as the Policy Decision Point in ZTA implementations.
      - name: Envoy Proxy
        description: Service mesh proxy enforcing mTLS and authorization policies as PEP.
      - name: Istio
        description: Kubernetes service mesh providing ZTA controls through SPIFFE and OPA integration.
      - name: HashiCorp Vault
        description: Secrets management platform providing dynamic credentials in ZTA pipelines.
      - name: Okta
        description: Identity provider for user and device authentication in ZTA implementations.
      - name: Microsoft Entra ID
        description: Cloud identity platform used as Identity Provider in enterprise ZTA deployments.
      - name: BeyondCorp Enterprise
        description: Google's ZTA implementation providing context-aware access for enterprise applications.
      - name: Cloudflare Zero Trust
        description: Zero Trust Network Access and secure web gateway platform.
      - name: Zscaler Private Access
        description: Cloud-native ZTNA solution providing ZTA-compliant access to private applications.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
