---
aid: zero-trust
name: Zero Trust
description: Zero Trust is the umbrella cybersecurity strategy that eliminates implicit trust based on network location and requires continuous verification of every user, device, workload, and access request. This index aggregates the core specifications (NIST, CISA, DoD, NSA, NCSC), the leading vendor platforms that implement Zero Trust (Cloudflare, Zscaler, Netskope, Palo Alto Networks, Tailscale, Twingate, Microsoft, Google), and the CNCF-graduated open standards that the ecosystem depends on (SPIFFE, SPIRE, OPA). Three sister API Evangelist topics cover Zero Trust Architecture, Zero Trust Network Access (ZTNA), and the Zero Trust Security Model in greater depth.
type: Index
url: https://www.nist.gov/publications/zero-trust-architecture
tags:
  - Access Control
  - Cloud Security
  - Cybersecurity
  - Federal
  - Identity and Access Management
  - Network Security
  - Security
  - Zero Trust
created: '2025'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: zero-trust:nist-sp-800-207
    name: NIST SP 800-207 Zero Trust Architecture
    description: The foundational US specification of Zero Trust, defining the seven tenets, PDP/PEP/PA components, and three deployment variants (enhanced identity governance, microsegmentation, network infrastructure / SDP).
    humanURL: https://csrc.nist.gov/pubs/sp/800/207/final
    tags:
      - NIST
      - Specification
    properties:
      - type: Documentation
        url: https://csrc.nist.gov/pubs/sp/800/207/final
      - type: APIReference
        url: https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-207.pdf
  - aid: zero-trust:cisa-ztmm
    name: CISA Zero Trust Maturity Model v2
    description: The federal-civilian Zero Trust roadmap from CISA, with four maturity levels across the Identity, Devices, Networks, Applications & Workloads, and Data pillars plus cross-cutting capabilities for Visibility & Analytics, Automation & Orchestration, and Governance.
    humanURL: https://www.cisa.gov/zero-trust-maturity-model
    tags:
      - CISA
      - Federal
      - Maturity Model
    properties:
      - type: Documentation
        url: https://www.cisa.gov/zero-trust-maturity-model
      - type: APIReference
        url: https://www.cisa.gov/sites/default/files/2023-04/zero_trust_maturity_model_v2_508.pdf
  - aid: zero-trust:dod-zt-ra
    name: DoD Zero Trust Reference Architecture
    description: The Department of Defense seven-pillar Zero Trust reference architecture and 152-capability target/advanced execution roadmap.
    humanURL: https://dodcio.defense.gov/library/
    tags:
      - DoD
      - Federal
      - Reference Architecture
    properties:
      - type: Documentation
        url: https://dodcio.defense.gov/Portals/0/Documents/Library/ZT-Reference-Architecture.pdf
  - aid: zero-trust:cloudflare-zero-trust
    name: Cloudflare Zero Trust API
    description: Cloudflare's Zero Trust platform combining ZTNA, SWG, CASB, RBI, DLP and an REST API for managing all of it.
    humanURL: https://developers.cloudflare.com/cloudflare-one/
    tags:
      - Cloudflare
      - SASE
      - Vendor
      - ZTNA
    properties:
      - type: Documentation
        url: https://developers.cloudflare.com/cloudflare-one/
      - type: APIReference
        url: https://developers.cloudflare.com/api/
  - aid: zero-trust:zscaler-zia-zpa
    name: Zscaler Zero Trust Exchange API
    description: Zscaler's combined ZIA (internet access) and ZPA (private access) Zero Trust platform with REST APIs for both.
    humanURL: https://help.zscaler.com/
    tags:
      - SASE
      - Vendor
      - Zscaler
    properties:
      - type: Documentation
        url: https://help.zscaler.com/
      - type: APIReference
        url: https://help.zscaler.com/zpa/api-reference
  - aid: zero-trust:microsoft-entra
    name: Microsoft Entra Zero Trust APIs
    description: Microsoft Entra (formerly Azure AD), Conditional Access, Defender for Cloud Apps, and Microsoft Intune together implement Zero Trust on the Microsoft platform; Microsoft Graph exposes a unified REST surface.
    humanURL: https://learn.microsoft.com/en-us/security/zero-trust/
    tags:
      - Microsoft
      - Vendor
      - IdP
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/security/zero-trust/
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/overview
  - aid: zero-trust:google-beyondcorp
    name: Google BeyondCorp Enterprise
    description: Google's productized Zero Trust platform building on the original BeyondCorp research; provides context-aware access through Identity-Aware Proxy and Chrome Enterprise.
    humanURL: https://cloud.google.com/beyondcorp-enterprise
    tags:
      - Google
      - Vendor
    properties:
      - type: Documentation
        url: https://cloud.google.com/beyondcorp-enterprise/docs
  - aid: zero-trust:spiffe-spire
    name: SPIFFE / SPIRE
    description: CNCF-graduated workload identity standard (SPIFFE) and reference runtime (SPIRE) used as the workload-identity foundation in Zero Trust deployments.
    humanURL: https://spiffe.io/
    tags:
      - CNCF
      - Open Source
      - Workload Identity
    properties:
      - type: Documentation
        url: https://spiffe.io/docs/latest/
      - type: GitHubOrganization
        url: https://github.com/spiffe
  - aid: zero-trust:open-policy-agent
    name: Open Policy Agent (OPA)
    description: CNCF-graduated general-purpose policy engine commonly deployed as the PDP in Zero Trust implementations.
    humanURL: https://www.openpolicyagent.org/
    tags:
      - CNCF
      - Open Source
      - Policy Engine
    properties:
      - type: Documentation
        url: https://www.openpolicyagent.org/docs/latest/
      - type: GitHubOrganization
        url: https://github.com/open-policy-agent
common:
  - type: Documentation
    title: NIST Zero Trust Architecture
    url: https://www.nist.gov/publications/zero-trust-architecture
  - type: Documentation
    title: NIST SP 800-207 PDF
    url: https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-207.pdf
  - type: Documentation
    title: NIST SP 800-207A PDF
    url: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207A.pdf
  - type: Compliance
    title: CISA Zero Trust Maturity Model v2
    url: https://www.cisa.gov/zero-trust-maturity-model
  - type: Compliance
    title: OMB M-22-09 Federal Zero Trust Strategy
    url: https://www.whitehouse.gov/wp-content/uploads/2022/01/M-22-09.pdf
  - type: Compliance
    title: DoD Zero Trust Reference Architecture
    url: https://dodcio.defense.gov/Portals/0/Documents/Library/ZT-Reference-Architecture.pdf
  - type: Documentation
    title: NSA Zero Trust Guidance
    url: https://www.nsa.gov/Press-Room/News-Highlights/Article/Article/2899282/nsa-releases-guidance-on-zero-trust-security-model/
  - type: Documentation
    title: UK NCSC Zero Trust Architecture
    url: https://www.ncsc.gov.uk/collection/zero-trust-architecture
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
    title: Microsoft Zero Trust Guidance Center
    url: https://learn.microsoft.com/en-us/security/zero-trust/
  - type: Portal
    title: Google BeyondCorp
    url: https://cloud.google.com/beyondcorp
  - type: Portal
    title: Tailscale
    url: https://tailscale.com/
  - type: Portal
    title: Twingate
    url: https://www.twingate.com/
  - type: GitHubOrganization
    title: SPIFFE
    url: https://github.com/spiffe
  - type: GitHubOrganization
    title: Open Policy Agent
    url: https://github.com/open-policy-agent
  - type: Resources
    title: Sister Topic - Zero Trust Architecture
    url: https://github.com/api-evangelist/zero-trust-architecture
  - type: Resources
    title: Sister Topic - Zero Trust Network Access
    url: https://github.com/api-evangelist/zero-trust-network-access
  - type: Resources
    title: Sister Topic - Zero Trust Security Model
    url: https://github.com/api-evangelist/zero-trust-security-model
  - type: JSONSchema
    title: Zero Trust Access Decision Schema
    url: json-schema/zero-trust-access-decision-schema.json
  - type: JSONSchema
    title: Zero Trust Subject Schema
    url: json-schema/zero-trust-subject-schema.json
  - type: JSONStructure
    title: Zero Trust Access Decision Structure
    url: json-structure/zero-trust-access-decision-structure.json
  - type: JSONLD
    title: Zero Trust JSON-LD Context
    url: json-ld/zero-trust-context.jsonld
  - type: CodeExamples
    title: Zero Trust Access Decision Example
    url: examples/zero-trust-access-decision-example.json
  - type: Resources
    title: Zero Trust Vocabulary
    url: vocabulary/zero-trust-vocabulary.yaml
  - type: Features
    data:
      - name: Identity Verification
        description: Authenticate every user and workload regardless of location.
      - name: Device Trust
        description: Continuously evaluate device posture before and during access.
      - name: Least Privilege
        description: Grant minimum required permissions per session.
      - name: Microsegmentation
        description: Limit lateral movement by segmenting workloads and networks.
      - name: Continuous Monitoring
        description: Continuously analyze signals and re-evaluate authorization.
      - name: Encryption Everywhere
        description: Use mTLS and end-to-end encryption between all components.
      - name: Policy as Code
        description: Author and version policy in machine-readable form (Rego, Cedar, JSON).
      - name: Assume Breach
        description: Design controls assuming attackers are already inside.
  - type: UseCases
    data:
      - name: VPN Modernization
        description: Replace flat-network VPNs with brokered, identity-aware access.
      - name: Federal Compliance
        description: Meet OMB M-22-09 Zero Trust mandate and CISA ZTMM milestones.
      - name: DoD Mission Adoption
        description: Implement the seven DoD Zero Trust pillars and 152 capabilities.
      - name: Multi-Cloud Workload Security
        description: Apply consistent Zero Trust controls across AWS, Azure, GCP.
      - name: Critical Infrastructure
        description: Apply Zero Trust to OT/ICS environments under TSA, NERC, and ENISA guidance.
      - name: Healthcare and Financial Compliance
        description: Align Zero Trust with HIPAA, GLBA, PCI-DSS, and SOX requirements.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
