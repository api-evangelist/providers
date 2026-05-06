---
aid: autotrac
name: AutoTrac
description: AutoTrac is a Brazilian fleet management and vehicle tracking technology company with over 30 years of experience. As the national market leader, AutoTrac provides satellite and cellular fleet tracking solutions, real-time telemetry, driver journey management, and management intelligence platforms for logistics, agriculture, maritime, and insurance sectors. The company operates its own terrestrial satellite communication station and data center for nationwide coverage.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Fleet Management
  - GPS Tracking
  - Telematics
  - Vehicle Tracking
  - Logistics
  - Brazil
  - Satellite Communication
url: https://raw.githubusercontent.com/api-evangelist/autotrac/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: autotrac:supervisor-web-api
    name: AutoTrac Supervisor Web API
    description: The AutoTrac Supervisor Web platform provides fleet management capabilities for monitoring vehicle locations, managing fleet operations, generating reports, and coordinating driver assignments across Brazil. API access enables third-party system integration with Supervisor Web data.
    humanURL: https://www.autotrac.com.br
    tags:
      - Fleet Management
      - GPS Tracking
      - Vehicle Monitoring
      - Fleet Operations
    properties:
      - type: Website
        url: https://www.autotrac.com.br
      - type: Documentation
        url: https://www.autotrac.com.br
  - aid: autotrac:telemetria-api
    name: AutoTrac Telemetria API
    description: The AutoTrac Telemetria platform provides real-time vehicle telemetry data including speed, fuel consumption, engine diagnostics, tire pressure, temperature sensors (for refrigerated cargo), and driver behavior metrics. Used for preventive maintenance and operational efficiency.
    humanURL: https://www.autotrac.com.br
    tags:
      - Telemetry
      - Vehicle Diagnostics
      - Fuel Management
      - Driver Behavior
    properties:
      - type: Website
        url: https://www.autotrac.com.br
  - aid: autotrac:jornada-api
    name: AutoTrac Jornada Driver Journey API
    description: The AutoTrac Jornada platform manages driver journey logs and compliance with Brazilian driving hour regulations, tracking driving time, rest periods, and journey records for long-distance transport compliance (Lei do Caminhoneiro).
    humanURL: https://www.autotrac.com.br
    tags:
      - Driver Management
      - Journey Logs
      - Compliance
      - Transportation Regulations
    properties:
      - type: Website
        url: https://www.autotrac.com.br
common:
  - type: Website
    url: https://www.autotrac.com.br
  - type: Features
    data:
      - name: Proprietary Satellite Communication
        description: AutoTrac operates its own terrestrial satellite communication station and integrated data center, providing coverage in areas with limited cellular connectivity across Brazil.
      - name: Real-Time Vehicle Telemetry
        description: Real-time monitoring of vehicle parameters including location, speed, fuel consumption, engine diagnostics, and cargo temperature for refrigerated transport.
      - name: Driver Journey Management
        description: Jornada platform for tracking driver hours, rest periods, and journey compliance with Brazilian transportation regulations.
      - name: Fleet Intelligence Reporting
        description: Informacoes Gerenciais business intelligence dashboards for fleet performance analytics, cost analysis, and operational reporting.
      - name: Agricultural Equipment Tracking
        description: Specialized tracking solutions for agricultural machinery including harvesters, tractors, and implements with field operation monitoring.
  - type: UseCases
    data:
      - name: Long-Distance Logistics Tracking
        description: Track trucks and cargo across Brazil using satellite and cellular communication for nationwide visibility of logistics operations.
      - name: Refrigerated Cargo Monitoring
        description: Monitor temperature-controlled cargo transport with real-time telemetry alerts for temperature deviations in refrigerated vehicles.
      - name: Driver Compliance Management
        description: Ensure compliance with Brazilian driver hour regulations by tracking journey logs and rest periods automatically via Jornada.
      - name: Agricultural Fleet Management
        description: Track agricultural equipment, monitor field operations, and manage harvest logistics for agribusiness operations.
      - name: Insurance Telematics
        description: Provide vehicle behavior and location data to insurance companies for usage-based insurance and stolen vehicle recovery programs.
  - type: Integrations
    data:
      - name: TMS Systems
        description: Integration with transportation management systems for freight dispatch, route optimization, and delivery confirmation workflows.
      - name: ERP Systems
        description: Connect AutoTrac fleet data with ERP systems (SAP, TOTVS) for fleet cost accounting, maintenance scheduling, and asset management.
      - name: Insurance Platforms
        description: API integration with insurance carriers for vehicle recovery, claims verification, and telematics-based premium calculation.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
