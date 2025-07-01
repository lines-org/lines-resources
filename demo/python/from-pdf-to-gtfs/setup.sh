LABEL=lines-gtfs-demo

STEPP_SOURCE=https://www.imt-ip.pt/sites/IMTT/Portugues/Planeamento/CooperacaoInternacional/ProgramasProjectosEuropeus/Documents/Dados%20multimodais/Ano%202023/ETAC%20-%20Empresa%20de%20Transportes%20Ant%C3%B3nio%20da%20Cunha.zip
STEPP_NAME=aveiro-bus
STEPP_FILE=resources/$STEPP_NAME.stepp.zip

PDF_SOURCE=https://www.aveirobus.pt/sites/default/files/horarios/aveiro-bus-site-horario-linha-297x297-l11-2024-04-0208.pdf
PDF_NAME=aveiro-bus-11
PDF_FILE=resources/$PDF_NAME.pdf

GTFS_VALIDATOR_SOURCE=https://github.com/MobilityData/gtfs-validator/releases/download/v6.0.0/gtfs-validator-6.0.0-cli.jar
GTFS_VALIDATOR_NAME=gtfs-validator
GTFS_VALIDATOR_FILE=resources/$GTFS_VALIDATOR_NAME.jar

[ ! -d resources ] && mkdir resources

# Setup Python virutal environment
if [ ! -d .venv ]; then
    echo "[$LABEL] Python virtual environment - not found, creating"
    python3 -m venv .venv
fi
echo "[$LABEL] Python virtual environment - created"

# Install Python requirements
echo "[$LABEL] Python requirements - installing"
source .venv/bin/activate
pip install -r requirements.txt > /dev/null
deactivate
echo "[$LABEL] Python requirements - installed"

# Install Java
if ! command -v java &> /dev/null; then
    echo "[$LABEL] Java - not found, installing"
    sudo apt-get install -y openjdk-17-jre-headless
fi
echo "[$LABEL] Java - installed"

# Collect STePP data from source
if [ ! -f $STEPP_FILE ]; then
    echo "[$LABEL] STePP data from Aveiro Bus - not found, collecting"
    curl -L $STEPP_SOURCE -o $STEPP_FILE
fi
echo "[$LABEL] STePP data from Aveiro Bus - collected ($STEPP_FILE)"

# Collect PDF file from source
if [ ! -f $PDF_FILE ]; then
    echo "[$LABEL] PDF file from Aveiro Bus L11 - not found, collecting"
    curl -L $PDF_SOURCE -o $PDF_FILE
fi
echo "[$LABEL] PDF file from Aveiro Bus L11 - collected ($PDF_FILE)"

# Collect Canonical GTFS Schedule Validator from source
if [ ! -f $GTFS_VALIDATOR_FILE ]; then
    echo "[$LABEL] Canonical GTFS Schedule Validator - not found, collecting"
    curl -L $GTFS_VALIDATOR_SOURCE -o $GTFS_VALIDATOR_FILE
fi
echo "[$LABEL] Canonical GTFS Schedule Validator - collected ($GTFS_VALIDATOR_FILE)"