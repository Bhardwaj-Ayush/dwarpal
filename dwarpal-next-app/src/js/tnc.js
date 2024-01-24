export default tnc = () => {
    document.addEventListener("DOMContentLoaded", () => {
        
        const { PythonShell } = require('python-shell');

        // Specify the path to the Python script
        const pythonScriptPath = "../scripts/tnc.py";

        // Create a PythonShell instance
        const pythonShell = new PythonShell(pythonScriptPath);

        // Handle messages from Python script
        pythonShell.on('message', (message) => {
            console.log(`Python script message: ${ message }`);
        });

        // Handle errors
        pythonShell.on('error', (err) => {
            console.error('Error executing Python script:', err);
        });

        // Execute the Python script
        pythonShell.end((err, code, signal) => {
            if (err) {
                console.error('Error during Python script execution:', err);
            } else {
                console.log('NLTK data downloaded successfully.');
            }
        });
    })
};
