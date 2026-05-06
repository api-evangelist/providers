---
aid: zero-trust-security-model
name: Zero-Trust Security Model
description: The Zero Trust security model is a strategic cybersecurity approach that eliminates implicit trust and requires continuous verification of every user, device, workload, and request attempting to access resources, regardless of network location. It is rooted in NIST SP 800-207, formalized for federal agencies by the CISA Zero Trust Maturity Model and the DoD Zero Trust Reference Architecture, and operationalized by NSA, NCSC, and industry guidance. This topic indexes the canonical specifications, guidance documents, advocacy organizations, and reference data schemas that describe the Zero Trust security model and its pillars (Identity, Devices, Networks, Applications & Workloads, Data, Visibility & Analytics, Automation & Orchestration).
type: Index
url: https://www.nist.gov/publications/zero-trust-architecture
tags:
  - Access Control
  - Cybersecurity
  - Federal
  - Identity Management
  - Network Security
  - NIST
  - Security
  - Security Framework
  - Zero Trust
created: '2025'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: zero-trust-security-model:nist-sp-800-207
    name: NIST SP 800-207 Zero Trust Architecture
    description: The foundational specification of the Zero Trust security model. Defines the seven tenets, the PDP/PEP/PA logical components, and the deployment variants (enhanced identity governance, microsegmentation, and network infrastructure / SDP).
    humanURL: https://csrc.nist.gov/pubs/sp/800/207/final
    tags:
      - NIST
      - Specification
      - Zero Trust
    properties:
      - type: Documentation
        url: https://csrc.nist.gov/pubs/sp/800/207/final
      - type: APIReference
        url: https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-207.pdf
  - aid: zero-trust-security-model:cisa-zero-trust-maturity-model
    name: CISA Zero Trust Maturity Model
    description: CISA's Zero Trust Maturity Model defines four maturity levels (Traditional, Initial, Advanced, Optimal) across five pillars (Identity, Devices, Networks, Applications & Workloads, Data) and three cross-cutting capabilities (Visibility & Analytics, Automation & Orchestration, Governance). It is the federal-civilian roadmap for Zero Trust adoption.
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
  - aid: zero-trust-security-model:dod-zero-trust-reference-architecture
    name: DoD Zero Trust Reference Architecture
    description: The Department of Defense Zero Trust Reference Architecture defines the seven DoD Zero Trust pillars (User, Device, Application & Workload, Data, Network & Environment, Automation & Orchestration, Visibility & Analytics) and 152 capabilities across target and advanced activities.
    humanURL: https://dodcio.defense.gov/library/
    tags:
      - DoD
      - Federal
      - Reference Architecture
    properties:
      - type: Documentation
        url: https://dodcio.defense.gov/Portals/0/Documents/Library/ZT-Reference-Architecture.pdf
  - aid: zero-trust-security-model:nsa-zero-trust-guidance
    name: NSA Zero Trust Guidance
    description: A series of NSA Cybersecurity Information Sheets providing pillar-by- pillar guidance for implementing Zero Trust, including the Network and Environment, User, Device, Application & Workload, and Data pillars.
    humanURL: https://www.nsa.gov/Cybersecurity/
    tags:
      - Federal
      - Guidance
      - NSA
    properties:
      - type: Documentation
        url: https://www.nsa.gov/Press-Room/News-Highlights/Article/Article/2899282/nsa-releases-guidance-on-zero-trust-security-model/
  - aid: zero-trust-security-model:ncsc-zero-trust-principles
    name: UK NCSC Zero Trust Architecture Design Principles
    description: The UK National Cyber Security Centre's eight Zero Trust design principles, providing the British government's view of Zero Trust architecture for both public-sector and private organizations.
    humanURL: https://www.ncsc.gov.uk/collection/zero-trust-architecture
    tags:
      - Guidance
      - NCSC
      - UK
    properties:
      - type: Documentation
        url: https://www.ncsc.gov.uk/collection/zero-trust-architecture
common:
  - type: Documentation
    title: NIST Zero Trust Architecture
    url: https://www.nist.gov/publications/zero-trust-architecture
    description: NIST landing page for Zero Trust Architecture publications.
  - type: Documentation
    title: NIST SP 800-207 PDF
    url: https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-207.pdf
  - type: Documentation
    title: NIST SP 800-207A PDF
    url: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207A.pdf
  - type: Compliance
    title: CISA Zero Trust Maturity Model
    url: https://www.cisa.gov/zero-trust-maturity-model
  - type: Compliance
    title: OMB M-22-09 Federal Zero Trust Strategy
    url: https://www.whitehouse.gov/wp-content/uploads/2022/01/M-22-09.pdf
    description: White House OMB memorandum mandating Zero Trust adoption across federal civilian agencies.
  - type: Compliance
    title: DoD Zero Trust Reference Architecture
    url: https://dodcio.defense.gov/Portals/0/Documents/Library/ZT-Reference-Architecture.pdf
  - type: Documentation
    title: NSA Zero Trust Guidance
    url: https://www.nsa.gov/Press-Room/News-Highlights/Article/Article/2899282/nsa-releases-guidance-on-zero-trust-security-model/
  - type: Documentation
    title: UK NCSC Zero Trust
    url: https://www.ncsc.gov.uk/collection/zero-trust-architecture
  - type: Portal
    title: Cloudflare Learning - What Is Zero Trust
    url: https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/
  - type: Portal
    title: Microsoft Zero Trust Guidance Center
    url: https://learn.microsoft.com/en-us/security/zero-trust/
  - type: Portal
    title: Google BeyondCorp
    url: https://cloud.google.com/beyondcorp
  - type: GitHubOrganization
    title: SPIFFE
    url: https://github.com/spiffe
  - type: GitHubOrganization
    title: Open Policy Agent
    url: https://github.com/open-policy-agent
  - type: JSONSchema
    title: Zero Trust Pillar Schema
    url: json-schema/zero-trust-security-model-pillar-schema.json
  - type: JSONSchema
    title: Zero Trust Maturity Assessment Schema
    url: json-schema/zero-trust-security-model-maturity-schema.json
  - type: JSONStructure
    title: Zero Trust Pillar Structure
    url: json-structure/zero-trust-security-model-pillar-structure.json
  - type: JSONLD
    title: Zero Trust Security Model JSON-LD Context
    url: json-ld/zero-trust-security-model-context.jsonld
  - type: CodeExamples
    title: Zero Trust Maturity Assessment Example
    url: examples/zero-trust-security-model-maturity-example.json
  - type: Resources
    title: Zero Trust Security Model Vocabulary
    url: vocabulary/zero-trust-security-model-vocabulary.yaml
  - type: Features
    data:
      - name: Never Trust Always Verify
        description: No user, device, or network is trusted by default; every access is verified.
      - name: Explicit Verification
        description: Authentication and authorization happen for every request using all available signals.
      - name: Least Privilege Access
        description: Users and workloads receive only the minimum permissions required for the task.
      - name: Assume Breach
        description: The model is designed assuming attackers are already present in the environment.
      - name: Continuous Monitoring
        description: All sessions and signals are continuously analyzed and policies re-evaluated.
      - name: Microsegmentation
        description: Networks and workloads are segmented to limit blast radius after compromise.
      - name: Data-Centric Protection
        description: Security controls follow the data, not the perimeter.
      - name: Identity as the Perimeter
        description: User and workload identity replaces network location as the primary trust boundary.
  - type: UseCases
    data:
      - name: Federal Civilian Compliance
        description: Meeting OMB M-22-09 and CISA Zero Trust Maturity Model requirements.
      - name: DoD Mission Systems
        description: Implementing the seven DoD Zero Trust pillars and 152 capabilities.
      - name: Critical Infrastructure
        description: Applying Zero Trust to OT and ICS environments in energy, water, and transportation.
      - name: Healthcare Data Protection
        description: Protecting PHI under HIPAA using Zero Trust controls and continuous verification.
      - name: Financial Services Compliance
        description: Aligning Zero Trust with SOX, GLBA, and PCI-DSS requirements.
      - name: Higher Education Research
        description: Securing distributed research networks and BYOD environments.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
