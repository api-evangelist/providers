---
aid: zero-trust-network-access
name: Zero Trust Network Access
description: Zero Trust Network Access (ZTNA) is a security framework and product category that grants access to private applications and resources based on identity, device posture, and context, rather than network location. ZTNA replaces the implicit trust of legacy VPNs with explicit per-request verification, creating one-to-one encrypted tunnels between authenticated users and the specific applications they are authorized to use. This topic collects the leading ZTNA vendors, the standards bodies that govern the underlying primitives, and the data schemas used to describe access policies, identities, devices, and resources.
type: Index
url: https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/
tags:
  - Access Control
  - Cloud Security
  - Cybersecurity
  - Identity Management
  - Network Access
  - Network Security
  - Security
  - VPN Replacement
  - Zero Trust
  - ZTNA
created: '2025'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: zero-trust-network-access:cloudflare-zero-trust
    name: Cloudflare Zero Trust API
    description: Cloudflare Zero Trust (formerly Cloudflare for Teams / Cloudflare Access) provides ZTNA, secure web gateway, browser isolation, CASB, and DLP through a single global edge platform. The Cloudflare API exposes endpoints for managing Access applications, policies, identity providers, device posture, tunnels, and gateway rules.
    humanURL: https://developers.cloudflare.com/cloudflare-one/
    tags:
      - Cloudflare
      - SASE
      - ZTNA
    properties:
      - type: Documentation
        url: https://developers.cloudflare.com/cloudflare-one/
      - type: APIReference
        url: https://developers.cloudflare.com/api/
      - type: Authentication
        url: https://developers.cloudflare.com/fundamentals/api/get-started/keys/
  - aid: zero-trust-network-access:zscaler-zpa
    name: Zscaler Private Access (ZPA) API
    description: Zscaler Private Access is a cloud-native ZTNA service that connects authenticated users to private applications without exposing them to the internet or placing them on the corporate network. The ZPA Public API supports application segments, server groups, policies, posture profiles, and connector groups.
    humanURL: https://help.zscaler.com/zpa/api-reference
    tags:
      - SASE
      - Zscaler
      - ZTNA
    properties:
      - type: Documentation
        url: https://help.zscaler.com/zpa
      - type: APIReference
        url: https://help.zscaler.com/zpa/api-reference
  - aid: zero-trust-network-access:netskope-private-access
    name: Netskope Private Access API
    description: Netskope Private Access provides ZTNA as part of the Netskope SASE platform, brokering authenticated access to private applications across cloud and on-premises. The Netskope REST API surfaces operations on private apps, publishers, policies, and risk events.
    humanURL: https://docs.netskope.com/en/netskope-help/admin-console/rest-api/
    tags:
      - Netskope
      - SASE
      - ZTNA
    properties:
      - type: Documentation
        url: https://docs.netskope.com/en/netskope-help/admin-console/rest-api/
  - aid: zero-trust-network-access:palo-alto-prisma-access
    name: Palo Alto Prisma Access (Prisma SASE) API
    description: Palo Alto Networks Prisma Access offers cloud-delivered ZTNA, SWG, and FWaaS as part of the Prisma SASE platform. The Prisma Access REST API exposes operations on remote networks, mobile users, security policies, and decryption rules.
    humanURL: https://docs.paloaltonetworks.com/prisma/prisma-access
    tags:
      - Palo Alto
      - SASE
      - ZTNA
    properties:
      - type: Documentation
        url: https://docs.paloaltonetworks.com/prisma/prisma-access
  - aid: zero-trust-network-access:tailscale-api
    name: Tailscale API
    description: Tailscale is a WireGuard-based mesh-VPN ZTNA platform that exposes a REST API for managing devices, ACL policies, tailnet keys, DNS, and audit logs. It implements identity-based device-to-device tunnels brokered by an identity-aware control plane.
    humanURL: https://tailscale.com/api
    tags:
      - Mesh VPN
      - Tailscale
      - WireGuard
      - ZTNA
    properties:
      - type: Documentation
        url: https://tailscale.com/api
      - type: APIReference
        url: https://tailscale.com/api
      - type: GitHubOrganization
        url: https://github.com/tailscale
  - aid: zero-trust-network-access:twingate-api
    name: Twingate API
    description: Twingate is a software-defined ZTNA platform that exposes a GraphQL Admin API for managing remote networks, resources, groups, users, service accounts, and connectors.
    humanURL: https://www.twingate.com/docs/api
    tags:
      - Twingate
      - ZTNA
    properties:
      - type: Documentation
        url: https://www.twingate.com/docs/api
      - type: APIReference
        url: https://www.twingate.com/docs/api
common:
  - type: Documentation
    title: Cloudflare - What Is Zero Trust
    url: https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/
    description: Cloudflare's reference explainer on Zero Trust security and ZTNA.
  - type: Documentation
    title: Gartner Definition of ZTNA
    url: https://www.gartner.com/en/information-technology/glossary/zero-trust-network-access-ztna-
    description: Gartner glossary entry defining ZTNA as a market category.
  - type: Documentation
    title: NIST SP 800-207 (ZTA underpinnings of ZTNA)
    url: https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-207.pdf
    description: NIST Special Publication 800-207 - the architectural foundation behind ZTNA.
  - type: Compliance
    title: CISA Zero Trust Maturity Model
    url: https://www.cisa.gov/zero-trust-maturity-model
    description: CISA Zero Trust Maturity Model that ZTNA deployments are commonly aligned to.
  - type: Portal
    title: Cloudflare Zero Trust
    url: https://www.cloudflare.com/zero-trust/
  - type: Portal
    title: Zscaler Zero Trust Exchange
    url: https://www.zscaler.com/products-and-solutions/zero-trust-exchange
  - type: Portal
    title: Netskope SASE
    url: https://www.netskope.com/platform/sase
  - type: Portal
    title: Palo Alto Networks Prisma Access
    url: https://www.paloaltonetworks.com/sase/access
  - type: Portal
    title: Tailscale
    url: https://tailscale.com/
  - type: Portal
    title: Twingate
    url: https://www.twingate.com/
  - type: GitHubOrganization
    title: Tailscale on GitHub
    url: https://github.com/tailscale
  - type: GitHubOrganization
    title: WireGuard
    url: https://github.com/WireGuard
  - type: JSONSchema
    title: ZTNA Access Policy Schema
    url: json-schema/zero-trust-network-access-policy-schema.json
  - type: JSONSchema
    title: ZTNA Application Schema
    url: json-schema/zero-trust-network-access-application-schema.json
  - type: JSONSchema
    title: ZTNA Device Posture Schema
    url: json-schema/zero-trust-network-access-device-posture-schema.json
  - type: JSONStructure
    title: ZTNA Access Policy Structure
    url: json-structure/zero-trust-network-access-policy-structure.json
  - type: JSONLD
    title: ZTNA JSON-LD Context
    url: json-ld/zero-trust-network-access-context.jsonld
  - type: CodeExamples
    title: ZTNA Access Policy Example
    url: examples/zero-trust-network-access-policy-example.json
  - type: CodeExamples
    title: ZTNA Device Posture Example
    url: examples/zero-trust-network-access-device-posture-example.json
  - type: Resources
    title: ZTNA Vocabulary
    url: vocabulary/zero-trust-network-access-vocabulary.yaml
  - type: Features
    data:
      - name: Identity-Centric Access
        description: Access decisions are based on user and workload identity rather than network location.
      - name: Application-Level Tunnels
        description: One-to-one encrypted connections between authenticated users and specific applications.
      - name: Device Posture Checks
        description: Continuous evaluation of device health, OS patch level, EDR status, and certificate state.
      - name: Context-Aware Policy
        description: Policies factor in time, location, risk score, and behavior in addition to identity.
      - name: Application Cloaking
        description: Private applications are dark to the public internet and not advertised by IP or DNS.
      - name: SSO and MFA Integration
        description: Native integration with SAML, OIDC, and modern MFA providers.
      - name: Microsegmentation
        description: Lateral movement is prevented by issuing scoped, per-application access.
      - name: Continuous Authorization
        description: Sessions are reauthenticated and reauthorized as conditions change.
  - type: UseCases
    data:
      - name: VPN Replacement
        description: Replacing legacy site-to-site and remote-access VPNs with identity-aware brokered access.
      - name: Third-Party Contractor Access
        description: Granting time-bounded, application-scoped access to vendors and contractors.
      - name: M&A Network Integration
        description: Enabling acquired companies to reach internal applications without merging networks.
      - name: BYOD Access
        description: Allowing personal and unmanaged devices to access selected applications under posture rules.
      - name: Privileged Access
        description: Brokering jump-host and bastion access to sensitive infrastructure.
      - name: Multi-Cloud Application Access
        description: Providing consistent ZTNA across applications hosted in AWS, Azure, GCP, and on-premises.
  - type: Integrations
    data:
      - name: Okta
        description: Enterprise identity provider used by virtually all ZTNA platforms.
      - name: Microsoft Entra ID
        description: Cloud identity platform integrated as IdP for ZTNA brokers.
      - name: CrowdStrike Falcon
        description: EDR signals fed into ZTNA device-posture rules.
      - name: SentinelOne
        description: EDR signals fed into ZTNA device-posture rules.
      - name: Jamf
        description: macOS / iOS MDM signals integrated into device posture for ZTNA.
      - name: Intune
        description: Microsoft Endpoint Manager signals integrated into device posture for ZTNA.
      - name: Splunk
        description: SIEM destination for ZTNA access and audit logs.
      - name: ServiceNow
        description: ITSM workflow integration for granting and revoking ZTNA access.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
