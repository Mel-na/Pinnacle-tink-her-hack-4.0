<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# [Astrashe] 🎯

## Basic Details

### Team Name: [Pinnacle] 

### Team Members
- Member 1: [Melna Rappai] - [ICCS COLLEGE OF ENGINEERING AND MANAGEMENT]
- Member 2: [Anupama P A] - [ICCS COLLEGE OF ENGINEERING AND MANAGEMENT]

### Hosted Project Link
[mention your project hosted link here]

### Project Description
[Astrashe is a web-based safe routing assistant designed to protect users navigating unfamiliar or potentially dangerous areas. It provides real-time secure navigation and features an instant "Danger Encountered" SOS system that immediately locates and routes users to the nearest verified safe havens.]
### The Problem statement
[When individuals travel through unfamiliar or unsafe environments, they often lack knowledge of secure routes. In moments of distress or imminent danger, panic makes it incredibly difficult to manually search for, locate, and navigate to the nearest reliable safe zones (such as police stations or hospitals), delaying critical help.]
### The Solution
[Astrashe acts as a proactive digital guardian. It allows users to search for their destination and generates a clear road route using mapping APIs. If a user feels threatened during their journey, a one-touch "Danger Encountered" button instantly queries geographic databases to find the closest police stations, hospitals, and women's help desks, providing immediate escape navigation and triggering simulated SOS alerts to trusted guardians.]
---

## Technical Details

### Technologies/Components Used

**For Software:**
- Languages used: [JavaScript, Python, HTML5,CSS3]
- Frameworks used: [FLASK,TALIWIND CSS]
- Libraries used: [Leaflet.js,OSRM API,Nomination API]
- Tools used: [VS Code, Git, Github]

**For Hardware:**
- No Hardware used.

---

## Features

List the key features of your project:
- Interactive Safe Routing: Dynamic map routing that draws real road paths from the user's current location to their searched destination.
- One-Touch Danger/SOS Protocol: An immediate override button that interrupts the journey and reroutes the user to verified safe zones if they feel threatened.
- Dynamic Safe Haven Locator: Uses real-time geographic APIs to scan the user's specific location for nearby Police Stations, General Hospitals, and Help Desks, including an offline-ready fallback system.
- Trusted Guardian Alerts: A system designed to automatically notify pre-set emergency contacts with live location tracking when the SOS protocol is triggered.

---

## Implementation

### For Software:

#### Installation
```bash
[# Clone the repository
git clone [Insert your GitHub Repo URL here]
cd [Your Repo Folder Name]

# Create a virtual environment (Recommended)
python -m venv venv
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

# Install the required dependencies
pip install flask]
```

#### Run
```bash
[# Start the Flask development server
python app.py

# The application will be available at http://127.0.0.1:5000]
```

## Project Documentation

### For Software:

#### Screenshots (Add at least 3)
[[alt text](image-2.png)]
*Add caption explaining what this shows*

[[alt text](image-1.png)]
*Add caption explaining what this shows*

[alt text](image.png)
*Add caption explaining what this shows*

#### Diagrams

**System Architecture:**

![Architecture Diagram](docs/architecture.png)
*Explain your system architecture - components, data flow, tech stack interaction*

**Application Workflow:**

[User logs in -> Searches Destination -> App generates OSRM route -> User travels. IF safe: arrives at destination. IF danger encountered: User clicks SOS -> App fetches Nominatim safe zones -> User selects safe zone -> App navigates to safety & alerts Guardians.]


---

### For Hardware:

#### Schematic & Circuit

![Circuit](Add your circuit diagram here)
*Add caption explaining connections*

![Schematic](Add your schematic diagram here)
*Add caption explaining the schematic*


---

## Additional Documentation

### For Web Projects with Backend:

#### API Documentation

**Base URL:** `https://api.yourproject.com`

##### Endpoints

**GET /api/endpoint**
- **Description:** [What it does]
- **Parameters:**
  - `param1` (string): [Description]
  - `param2` (integer): [Description]
- **Response:**
```json
{
  "status": "success",
  "data": {}
}
```

**POST /api/endpoint**
- **Description:** [What it does]
- **Request Body:**
```json
{
  "field1": "value1",
  "field2": "value2"
}
```
- **Response:**
```json
{
  "status": "success",
  "message": "Operation completed"
}
```

[Add more endpoints as needed...]

---

### For Mobile Apps:

#### App Flow Diagram

![App Flow](docs/app-flow.png)
*Explain the user flow through your application*

#### Installation Guide

**For Android (APK):**
1. Download the APK from [Release Link]
2. Enable "Install from Unknown Sources" in your device settings:
   - Go to Settings > Security
   - Enable "Unknown Sources"
3. Open the downloaded APK file
4. Follow the installation prompts
5. Open the app and enjoy!

**For iOS (IPA) - TestFlight:**
1. Download TestFlight from the App Store
2. Open this TestFlight link: [Your TestFlight Link]
3. Click "Install" or "Accept"
4. Wait for the app to install
5. Open the app from your home screen

**Building from Source:**
```bash
# For Android
flutter build apk
# or
./gradlew assembleDebug

# For iOS
flutter build ios
# or
xcodebuild -workspace App.xcworkspace -scheme App -configuration Debug
```

---

### For Hardware Projects:

#### Bill of Materials (BOM)

| Component | Quantity | Specifications | Price | Link/Source |
|-----------|----------|----------------|-------|-------------|
| Arduino Uno | 1 | ATmega328P, 16MHz | ₹450 | [Link] |
| LED | 5 | Red, 5mm, 20mA | ₹5 each | [Link] |
| Resistor | 5 | 220Ω, 1/4W | ₹1 each | [Link] |
| Breadboard | 1 | 830 points | ₹100 | [Link] |
| Jumper Wires | 20 | Male-to-Male | ₹50 | [Link] |
| [Add more...] | | | | |

**Total Estimated Cost:** ₹[Amount]

#### Assembly Instructions

**Step 1: Prepare Components**
1. Gather all components listed in the BOM
2. Check component specifications
3. Prepare your workspace
![Step 1](images/assembly-step1.jpg)
*Caption: All components laid out*

**Step 2: Build the Power Supply**
1. Connect the power rails on the breadboard
2. Connect Arduino 5V to breadboard positive rail
3. Connect Arduino GND to breadboard negative rail
![Step 2](images/assembly-step2.jpg)
*Caption: Power connections completed*

**Step 3: Add Components**
1. Place LEDs on breadboard
2. Connect resistors in series with LEDs
3. Connect LED cathodes to GND
4. Connect LED anodes to Arduino digital pins (2-6)
![Step 3](images/assembly-step3.jpg)
*Caption: LED circuit assembled*

**Step 4: [Continue for all steps...]**

**Final Assembly:**
![Final Build](images/final-build.jpg)
*Caption: Completed project ready for testing*

---

### For Scripts/CLI Tools:

#### Command Reference

**Basic Usage:**
```bash
python script.py [options] [arguments]
```

**Available Commands:**
- `command1 [args]` - Description of what command1 does
- `command2 [args]` - Description of what command2 does
- `command3 [args]` - Description of what command3 does

**Options:**
- `-h, --help` - Show help message and exit
- `-v, --verbose` - Enable verbose output
- `-o, --output FILE` - Specify output file path
- `-c, --config FILE` - Specify configuration file
- `--version` - Show version information

**Examples:**

```bash
# Example 1: Basic usage
python script.py input.txt

# Example 2: With verbose output
python script.py -v input.txt

# Example 3: Specify output file
python script.py -o output.txt input.txt

# Example 4: Using configuration
python script.py -c config.json --verbose input.txt
```

#### Demo Output

**Example 1: Basic Processing**

**Input:**
```
This is a sample input file
with multiple lines of text
for demonstration purposes
```

**Command:**
```bash
python script.py sample.txt
```

**Output:**
```
Processing: sample.txt
Lines processed: 3
Characters counted: 86
Status: Success
Output saved to: output.txt
```

**Example 2: Advanced Usage**

**Input:**
```json
{
  "name": "test",
  "value": 123
}
```

**Command:**
```bash
python script.py -v --format json data.json
```

**Output:**
```
[VERBOSE] Loading configuration...
[VERBOSE] Parsing JSON input...
[VERBOSE] Processing data...
{
  "status": "success",
  "processed": true,
  "result": {
    "name": "test",
    "value": 123,
    "timestamp": "2024-02-07T10:30:00"
  }
}
[VERBOSE] Operation completed in 0.23s
```

---

## Project Demo

### Video
[https://drive.google.com/file/d/1pXGgVksoGo0bH_gMEX0xSnZcDo1_9muu/view?usp=sharing.]

*Explain what the video demonstrates - key features, user flow, technical highlights*

### Additional Demos
[Add any extra demo materials/links - Live site, APK download, online demo, etc.]

---

## AI Tools Used (Optional - For Transparency Bonus)

If you used AI tools during development, document them here for transparency:

**Tool Used:** [e.g., GitHub Copilot, v0.dev, Cursor, ChatGPT, Claude]

**Purpose:** [What you used it for]
- Example: "Generated boilerplate React components"
- Example: "Debugging assistance for async functions"
- Example: "Code review and optimization suggestions"

**Key Prompts Used:**
- "Create a REST API endpoint for user authentication"
- "Debug this async function that's causing race conditions"
- "Optimize this database query for better performance"

**Percentage of AI-generated code:** [Approximately X%]

**Human Contributions:**
- Architecture design and planning
- Custom business logic implementation
- Integration and testing
- UI/UX design decisions

*Note: Proper documentation of AI usage demonstrates transparency and earns bonus points in evaluation!*

---

## Team Contributions

- [Melna Rappai]: [ Frontend UI development with Tailwind CSS, integrating Leaflet maps, debugging the search routing]
- [Anupama P.A]: [ Flask backend setup, API integration (OSRM/Nominatim), implementing the SOS fallback logic and project documentation.]

## License

This project is licensed under the [LICENSE_NAME] License - see the [LICENSE](LICENSE) file for details.

**Common License Options:**
- MIT License (Permissive, widely used)
- Apache 2.0 (Permissive with patent grant)
- GPL v3 (Copyleft, requires derivative works to be open source)

---

Made with ❤️ at TinkerHub

