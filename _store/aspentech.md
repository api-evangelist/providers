---
aid: aspentech
url: https://raw.githubusercontent.com/api-evangelist/aspentech/refs/heads/main/apis.yml
name: AspenTech
description: AspenTech (Aspen Technology, Inc.) is a global leader in industrial software for asset optimization across the energy, chemicals, and manufacturing industries. AspenTech provides process simulation, optimization, and industrial IoT platforms including the aspenONE suite and Inmation industrial data platform. The Inmation platform provides Web API and Simple Call Interface (SCI) APIs for external applications to interact with industrial IoT and time-series process data via HTTP and WebSocket interfaces. AspenTech serves refineries, petrochemical plants, power generation facilities, and other industrial operations worldwide.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Industrial IoT
  - Process Optimization
  - Manufacturing
  - Energy
  - Chemicals
  - Time Series
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: aspentech:inmation-web-api
    name: AspenTech Inmation Web API
    description: The AspenTech Inmation Web API provides HTTP and WebSocket interfaces for external applications to interact with AspenTech Inmation industrial IoT and time-series data platforms. RPC-based REST APIs enable access to process data, system services, and automation functions for manufacturing and energy operations.
    humanURL: https://atdocs.inmation.com/api/1.108/webapi/index.html
    baseURL: http://hostname:8002
    tags:
      - Industrial IoT
      - Manufacturing
      - Process Optimization
      - REST
      - Time Series
      - WebSocket
    properties:
      - type: Documentation
        url: https://atdocs.inmation.com/api/1.108/webapi/index.html
      - type: OpenAPI
        url: openapi/aspentech-inmation-web-openapi.yml
      - type: JSONSchema
        url: json-schema/aspentech-dataitem-schema.json
  - aid: aspentech:aspenone-api
    name: AspenTech aspenONE API
    description: AspenTech provides process optimization and simulation software for energy, chemicals, and manufacturing industries. The aspenONE platform APIs enable access to process simulation models, performance monitoring, and optimization data for AI-driven operational workflows.
    humanURL: https://www.aspentech.com/
    baseURL: https://api.aspentech.com
    tags:
      - Energy
      - Manufacturing
      - Process Engineering
      - Process Optimization
      - Simulation
    properties:
      - type: GettingStarted
        url: https://www.aspentech.com/en/getting-started-guides
      - type: Documentation
        url: https://dev.knowledgecenter.aspentech.com/
  - aid: aspentech:inmation-sci-api
    name: AspenTech Inmation Simple Call Interface (SCI) API
    description: The AspenTech Inmation Simple Call Interface (SCI) API provides a simplified HTTP interface for communicating with the Inmation industrial data platform. Designed for straightforward read/write access to process data and configuration items in manufacturing and energy environments.
    humanURL: https://atdocs.inmation.com/api/1.102/sci/index.html
    baseURL: http://hostname:8002
    tags:
      - Industrial IoT
      - Manufacturing
      - Process Optimization
      - REST
    properties:
      - type: Documentation
        url: https://atdocs.inmation.com/api/1.102/sci/index.html
common:
  - type: Portal
    url: https://www.aspentech.com/
    title: AspenTech Website
  - type: Portal
    url: https://dev.knowledgecenter.aspentech.com/
    title: Developer Knowledge Center
  - type: Documentation
    url: https://dev.knowledgecenter.aspentech.com/
    title: Documentation
  - type: GettingStarted
    url: https://www.aspentech.com/en/getting-started-guides
    title: Getting Started Guides
  - type: Support
    url: https://esupport.aspentech.com/
    title: Technical Support
  - type: OpenAPI
    url: openapi/aspentech-inmation-web-openapi.yml
    title: Inmation Web API OpenAPI
  - type: JSONSchema
    url: json-schema/aspentech-dataitem-schema.json
    title: Data Item JSON Schema
  - type: JSONLD
    url: json-ld/aspentech-context.jsonld
    title: AspenTech JSON-LD Context
  - type: Features
    data:
      - name: Inmation Industrial IoT Platform
        description: The Inmation platform provides industrial-grade time-series data management, process data connectivity, and real-time analytics for manufacturing and energy operations.
      - name: Process Simulation
        description: aspenONE suite provides high-fidelity process simulation for design, optimization, and operational decision support in chemical plants, refineries, and energy facilities.
      - name: WebSocket Real-Time Data
        description: WebSocket interface in the Inmation Web API enables real-time streaming of process data, alarm states, and operational events to external applications.
      - name: Asset Performance Management
        description: Tools for monitoring asset health, predicting maintenance needs, and optimizing equipment performance across industrial operations.
      - name: AI/ML Integration
        description: APIs for integrating AI and machine learning models with process data to enable predictive analytics and autonomous optimization.
  - type: UseCases
    data:
      - name: Process Data Integration
        description: Operations technology teams integrate the Inmation Web API with business intelligence tools, historian systems, and enterprise applications to access real-time and historical process data.
      - name: Digital Twin Development
        description: Engineering teams use aspenONE simulation APIs to build digital twins of process plants for operations optimization and scenario analysis.
      - name: Alarm Management
        description: Control systems engineers use the Inmation API to build custom alarm management dashboards and analytics for industrial operations.
      - name: Energy Optimization
        description: Refineries and petrochemical plants use AspenTech APIs to connect optimization models with real-time operations for energy efficiency.
  - type: Integrations
    data:
      - name: OSIsoft PI System
        description: AspenTech integrates with OSIsoft PI (now AVEVA PI) for process data historian connectivity and operational data access.
      - name: SAP
        description: Enterprise integration with SAP ERP systems for maintenance, production, and procurement data exchange.
      - name: AVEVA
        description: Integration with AVEVA engineering and operations management platforms for plant lifecycle data management.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
