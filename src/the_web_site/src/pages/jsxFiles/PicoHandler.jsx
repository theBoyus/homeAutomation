export default async function PicoHandler(action) {
    const picoIP = 'http://192.168.166.140';
    const endpoint = `/api/${action}`;

    try {
        const response = await fetch(picoIP + endpoint);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        return data;
    } catch (error) {
        console.error("Error fetching data: ", error);
    }
}
