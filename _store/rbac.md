---
aid: rbac
name: RBAC
description: 'Role-Based Access Control (RBAC) is a security paradigm that restricts system access based on assigned roles rather than individual user identities. Users are granted permissions through role membership, simplifying access management and ensuring the principle of least privilege. RBAC is foundational to enterprise identity, authorization, and compliance programs and is implemented across operating systems, cloud platforms, databases, and APIs. The NIST/ANSI/INCITS 359-2004 standard formally defines the RBAC model across four components: Core RBAC, Hierarchical RBAC, Static Separation of Duty, and Dynamic Separation of Duty. Cloud platforms (AWS IAM, Azure RBAC, GCP IAM) and Kubernetes all implement RBAC natively, making it the de facto authorization standard for enterprise and cloud-native environments.'
type: Index
position: Consuming
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/rbac/refs/heads/main/apis.yml
tags:
  - Access Control
  - Authorization
  - Cloud Native
  - Compliance
  - Identity Management
  - Kubernetes
  - RBAC
  - Security
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis: []
common:
  - type: JSONSchema
    name: RBAC Role Schema
    description: JSON Schema definition for an RBAC role.
    url: https://raw.githubusercontent.com/api-evangelist/rbac/refs/heads/main/json-schema/rbac-role.json
  - type: JSONSchema
    name: RBAC Permission Schema
    description: JSON Schema definition for an RBAC permission.
    url: https://raw.githubusercontent.com/api-evangelist/rbac/refs/heads/main/json-schema/rbac-permission.json
  - type: JSONSchema
    name: RBAC Assignment Schema
    description: JSON Schema definition for assigning roles to users.
    url: https://raw.githubusercontent.com/api-evangelist/rbac/refs/heads/main/json-schema/rbac-assignment.json
  - type: JSONStructure
    name: RBAC Role Structure
    description: Field-level structure documentation for the RBAC role object.
    url: https://raw.githubusercontent.com/api-evangelist/rbac/refs/heads/main/json-structure/rbac-role-structure.json
  - type: JSONStructure
    name: RBAC Permission Structure
    description: Field-level structure documentation for the RBAC permission object.
    url: https://raw.githubusercontent.com/api-evangelist/rbac/refs/heads/main/json-structure/rbac-permission-structure.json
  - type: JSONStructure
    name: RBAC Assignment Structure
    description: Field-level structure documentation for the RBAC role assignment object.
    url: https://raw.githubusercontent.com/api-evangelist/rbac/refs/heads/main/json-structure/rbac-assignment-structure.json
  - type: JSONLDContext
    name: RBAC JSON-LD Context
    description: JSON-LD context mapping RBAC vocabulary to linked data identifiers.
    url: https://raw.githubusercontent.com/api-evangelist/rbac/refs/heads/main/json-ld/rbac-context.jsonld
  - type: Example
    name: RBAC Role Example
    description: Example RBAC role object for a Content Editor.
    url: https://raw.githubusercontent.com/api-evangelist/rbac/refs/heads/main/examples/rbac-role-example.json
  - type: Example
    name: RBAC Permission Example
    description: Example RBAC permission object for publishing content.
    url: https://raw.githubusercontent.com/api-evangelist/rbac/refs/heads/main/examples/rbac-permission-example.json
  - type: Example
    name: RBAC Assignment Example
    description: Example RBAC role assignment binding a user to the Content Editor role.
    url: https://raw.githubusercontent.com/api-evangelist/rbac/refs/heads/main/examples/rbac-assignment-example.json
  - type: Vocabulary
    name: RBAC Vocabulary
    description: Domain vocabulary for RBAC concepts, terms, and implementation patterns.
    url: https://raw.githubusercontent.com/api-evangelist/rbac/refs/heads/main/vocabulary/rbac-vocabulary.yml
  - type: Standard
    name: ANSI/INCITS 359-2012 RBAC Standard
    description: The American National Standard for Role-Based Access Control.
    url: https://csrc.nist.gov/projects/role-based-access-control
  - type: Documentation
    name: Kubernetes RBAC Authorization
    description: Official Kubernetes documentation for RBAC authorization.
    url: https://kubernetes.io/docs/reference/access-authn-authz/rbac/
  - type: Documentation
    name: AWS IAM Role-Based Access Control
    description: AWS Identity and Access Management RBAC documentation.
    url: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
