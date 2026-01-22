# Python Support Toolkit

Production-style Python utilities for application support engineers and
customer success teams working with SaaS and cloud platforms.

This repository contains small scripts used during incident response,
API troubleshooting, and infrastructure validation.

## Tools

- log_errors.py – scan logs and surface the most common ERROR messages
- api_health_check.py – check HTTP endpoints and response latency
- system_snapshot.py – capture CPU, memory, disk, and running processes
- port_check.py – test TCP connectivity to a host and port
- restart_service.py – example script to restart a Linux service

## Typical Use Cases

- Production incident triage
- API debugging
- Cloud connectivity checks
- Root-cause analysis
- Customer escalation support

## Requirements

Python 3.9+

## Example Usage

python log_errors.py /var/log/app.log

python api_health_check.py https://api.example.com/health

python system_snapshot.py

python port_check.py google.com 443
