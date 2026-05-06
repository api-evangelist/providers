---
aid: agilent-technologies
url: https://raw.githubusercontent.com/api-evangelist/agilent-technologies/refs/heads/main/apis.yml
modified: '2026-04-19'
description: Agilent Technologies is a global leader in life sciences, diagnostics, and applied chemical markets, providing instruments, software, services, and consumables for laboratory workflows. Agilent offers APIs for laboratory operations management including iLab for core facility billing and scheduling, SLIMS for laboratory information management, CrossLab Asset Manager for instrument management, and VWorks for laboratory automation.
tags:
  - Life Sciences
  - Diagnostics
  - Laboratory
  - Scientific Instruments
  - LIMS
  - Laboratory Automation
apis:
  - name: Agilent iLab Operations API
    description: The iLab API enables customers to seamlessly integrate outside applications with iLab's billing and reporting modules. It leverages a RESTful application architecture with HATEOAS (Hypermedia as the Engine of Application State) and OAuth2 for secure access. The API supports integrations with institutional financial systems such as SAP, Oracle/PeopleSoft, Lawson, and Banner, as well as identity management systems and LIMS.
    humanURL: https://help.ilab.agilent.com/ilab-api
    baseURL: https://api.ilabsolutions.com/v1
    tags:
      - Laboratory Operations
      - Billing
      - Core Facilities
      - Scheduling
    properties:
      - type: Documentation
        url: https://help.ilab.agilent.com/ilab-api
      - type: Authentication
        url: https://help.ilab.agilent.com/ilab-api
      - type: OpenAPI
        url: openapi/agilent-ilab-operations-api.yaml
      - type: JSONSchema
        url: json-schema/ilab-operations-api-core-schema.json
        title: Core Schema
      - type: JSONSchema
        url: json-schema/ilab-operations-api-service-schema.json
        title: Service Schema
      - type: JSONSchema
        url: json-schema/ilab-operations-api-service-request-schema.json
        title: Service Request Schema
      - type: JSONSchema
        url: json-schema/ilab-operations-api-reservation-schema.json
        title: Reservation Schema
      - type: JSONSchema
        url: json-schema/ilab-operations-api-invoice-schema.json
        title: Invoice Schema
      - type: JSONSchema
        url: json-schema/ilab-operations-api-member-schema.json
        title: Member Schema
      - type: JSONSchema
        url: json-schema/ilab-operations-api-project-schema.json
        title: Project Schema
      - type: JSONStructure
        url: json-structure/ilab-operations-api-core-structure.json
        title: Core Structure
      - type: JSONStructure
        url: json-structure/ilab-operations-api-service-request-structure.json
        title: Service Request Structure
      - type: JSON-LD
        url: json-ld/agilent-ilab-operations-api-context.jsonld
  - name: Agilent SLIMS REST API
    description: The SLIMS (Smart Laboratory Information Management System) REST API provides programmatic access to Agilent SLIMS laboratory data management platform. SLIMS features three APIs — REST, Java, and Python — enabling integration with analytical instruments, NGS workflows, biobanks, and R&D labs. The REST API is auto-documented within each SLIMS instance.
    humanURL: https://slims-python-api.readthedocs.io/
    baseURL: https://your-slims-instance/rest
    tags:
      - LIMS
      - Laboratory Information Management
      - NGS
      - Biobank
    properties:
      - type: Documentation
        url: https://community.agilent.com/cfs-file/__key/docpreview-s/00-00-02-00-89/slims_5F00_development_5F00_manual_2D00_6.9.29.pdf
        title: SLIMS Development Manual v6.9
      - type: SDK
        url: https://github.com/genohm/slims-python-api
        title: Python SDK
      - type: SDK
        url: https://github.com/genohm/slims-api
        title: Plugin API
  - name: Agilent CrossLab Asset Manager API
    description: The CrossLab Asset Manager API provides programmatic access to Agilent's CrossLab instrument services platform, enabling management of laboratory assets, instrument service records, maintenance scheduling, and compliance tracking across laboratory environments.
    humanURL: https://crosslab-api.agilent.com/
    baseURL: https://crosslab-api.agilent.com
    tags:
      - Asset Management
      - Instrument Services
      - CrossLab
      - Maintenance
    properties:
      - type: Documentation
        url: https://crosslab-api.agilent.com/
  - name: Agilent VWorks Automation API
    description: The VWorks API provides a Component Object Model (COM) application programming interface for VWorks laboratory automation software (version 14.0 and later). It enables programmatic control of laboratory workstations, automated liquid handling robots, and integrated automation systems.
    humanURL: https://www.agilent.com/cs/library/usermanuals/public/D0008025_VWorks_API_Reference_Agilent.pdf
    baseURL: https://www.agilent.com
    tags:
      - Laboratory Automation
      - Robotics
      - Liquid Handling
      - Workstation
    properties:
      - type: Documentation
        url: https://www.agilent.com/cs/library/usermanuals/public/D0008025_VWorks_API_Reference_Agilent.pdf
        title: VWorks API Reference Guide v14.0
common:
  - type: Website
    url: https://www.agilent.com/en
  - type: Support
    url: https://www.agilent.com/en/support
  - type: Community
    url: https://community.agilent.com
  - type: GitHubOrganization
    url: https://github.com/Agilent
  - type: TermsOfService
    url: https://www.agilent.com/en/legal
  - type: PrivacyPolicy
    url: https://www.agilent.com/en/privacy-statement
  - type: SpectralRules
    url: rules/agilent-technologies-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/laboratory-operations.yaml
  - type: Vocabulary
    url: vocabulary/agilent-technologies-vocabulary.yaml
  - type: Features
    data:
      - name: RESTful Architecture
        description: iLab and CrossLab APIs leverage RESTful architecture with HATEOAS for discoverable resource navigation.
      - name: OAuth2 Authentication
        description: Secure access to APIs via OAuth2 with client ID and API token-based authentication.
      - name: Financial System Integration
        description: Pre-built integration support for SAP, Oracle/PeopleSoft, Lawson, and Banner financial systems.
      - name: LIMS Integration
        description: Integration with laboratory information management systems for sample tracking and results management.
      - name: Instrument Data Import
        description: Ability to import usage logs and data directly from connected laboratory instruments.
      - name: Plugin Architecture
        description: SLIMS supports custom plugin development via Java and Python APIs for workflow extension.
      - name: Auto-Generated API Documentation
        description: SLIMS REST API documentation is automatically generated from each deployed instance.
  - type: UseCases
    data:
      - name: Core Facility Billing Automation
        description: Automate billing workflows between iLab core facilities and institutional financial systems such as SAP or Oracle.
      - name: Laboratory Scheduling Integration
        description: Integrate external scheduling applications with iLab's equipment reservation and usage tracking.
      - name: Sample Lifecycle Management
        description: Use the SLIMS API to track samples from receipt through analysis and reporting across NGS, biobank, and R&D workflows.
      - name: Instrument Asset Tracking
        description: Manage laboratory instrument service records, calibration schedules, and compliance documentation via CrossLab Asset Manager API.
      - name: Automation Workflow Control
        description: Programmatically control VWorks-driven liquid handling robots and integrated workstations for high-throughput workflows.
      - name: LIMS Data Reporting
        description: Extract and aggregate laboratory data from SLIMS for custom reporting and business intelligence integrations.
  - type: Integrations
    data:
      - name: SAP
        description: Financial system integration for billing and cost accounting via iLab API.
      - name: Oracle PeopleSoft
        description: ERP integration for institutional billing and financial reporting.
      - name: Lawson
        description: Financial management system integration for laboratory billing workflows.
      - name: Banner
        description: Higher education ERP integration for core facility cost center management.
      - name: LabWare LIMS
        description: Integration between Agilent instruments and LabWare LIMS for data transfer and workflow coordination.
      - name: Identity Management Systems
        description: Integration with institutional identity providers for single sign-on and user provisioning.
---
