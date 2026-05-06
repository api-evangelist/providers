---
aid: american-airlines
name: American Airlines
description: American Airlines is one of the world's largest airlines, operating an extensive domestic and international route network. The company's Runway developer experience platform, built on Spotify's Backstage, provides internal developer tooling and API management for engineering teams. American Airlines exposes flight data, status, and booking capabilities through its developer portal, and maintains an active open-source presence via the AmericanAirlines GitHub organization.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Airlines
  - Aviation
  - Flights
  - Travel
  - Booking
  - Developer Experience
url: https://raw.githubusercontent.com/api-evangelist/american-airlines/refs/heads/main/apis.yml
created: '2026-04-19'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: american-airlines:runway-developer-api
    name: American Airlines Runway Developer API
    description: Runway is American Airlines' developer experience platform providing APIs for flight operations, booking, scheduling, and travel services. Built on Spotify's Backstage platform, Runway serves as the central hub for American Airlines API integrations with built-in API management, security, and authentication capabilities. Teams can deploy running apps with public ingress in under six minutes.
    humanURL: https://developer.aa.com/
    baseURL: https://developer.aa.com/api
    tags:
      - Airlines
      - Aviation
      - Flights
      - Travel
      - Booking
    properties:
      - type: Documentation
        url: https://developer.aa.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/american-airlines/refs/heads/main/openapi/american-airlines-runway-developer-api-openapi.yml
common:
  - type: Website
    url: https://www.aa.com/
  - type: DeveloperPortal
    url: https://developer.aa.com/
  - type: GitHubOrganization
    url: https://github.com/AmericanAirlines
  - type: Blog
    url: https://tech.aa.com/
  - type: GitHubRepository
    url: https://github.com/AmericanAirlines/backstage
  - type: Tools
    url: https://github.com/AmericanAirlines/Flight-Engine
    title: Flight Engine Mock API
  - type: Tools
    url: https://github.com/AmericanAirlines/Hangar
    title: Hangar Hackathon Tool
  - type: Features
    data:
      - name: Runway Developer Experience Platform
        description: Internal developer platform built on Spotify's Backstage providing centralized API management, service catalog, and self-service infrastructure tooling for engineering teams.
      - name: Flight Data APIs
        description: APIs for querying flight schedules, routes, status information, and operational data across American Airlines' domestic and international network.
      - name: Booking and Reservation APIs
        description: APIs supporting flight search, booking, reservation management, and passenger services integration for travel applications.
      - name: Built-In API Management
        description: Runway provides integrated API management with security, authentication toggles, and corporate authentication capabilities for development teams.
      - name: Service Mesh Integration
        description: Kong-based service mesh enabling reliable microservices communication and traffic management across the American Airlines platform.
      - name: Open Source Tooling
        description: American Airlines maintains open-source tools including Flight Engine (mock flight data API), Hangar (hackathon management), and Backstage plugins via the AmericanAirlines GitHub organization.
  - type: UseCases
    data:
      - name: Flight Search and Booking
        description: Travel agencies and booking platforms integrate flight availability, pricing, and reservation APIs to offer American Airlines flights.
      - name: Flight Status Tracking
        description: Applications query real-time flight status, departure, arrival, and delay information for American Airlines flights.
      - name: Internal Developer Tooling
        description: American Airlines engineering teams use Runway to self-service infrastructure, register APIs in the service catalog, and manage deployments.
      - name: Hackathon and Innovation
        description: Open-source Hangar tool enables hackathon management for tech innovation events sponsored by or affiliated with American Airlines.
  - type: Integrations
    data:
      - name: Spotify Backstage
        description: Runway developer portal is built on Spotify's Backstage platform for internal developer experience and service catalog management.
      - name: Kong Service Mesh
        description: American Airlines uses Kong's Kuma service mesh for microservices networking and API gateway capabilities.
      - name: HashiCorp Vault
        description: Integration with HashiCorp Vault for secrets management in build pipelines via open-source vault-action GitHub Action.
      - name: Dynatrace
        description: Python API client for Dynatrace integration maintained in the AmericanAirlines GitHub organization.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
