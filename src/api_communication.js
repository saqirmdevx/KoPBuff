import axios from "axios"
import { decode } from "msgpackr/unpack";
import { Buffer } from "buffer";

const debug = 0;


// API documentation:  https://github.com/saqirmdevx/LoP2_Server/blob/develop/gameServer/src/api/public/documentation.md

const domain = debug && "http://localhost:3000" || "https://eu.leagueofpixels.eu"

const API_URL = `${domain}/api/public`

const API_ENDPOINTS = {
    heroes: "heroes",
    items: "items",
    player: "player",
    match: "match",
    matches: "matches",
    leaderboard: "leaderboard",
}

const ASSETS_URL = `${domain}/assets2`

const ASSETS_ENDPOINTS = {
    heroes: "creatures/heroes",
    items: "items/itemUsed"
}


const getHeroAssetURL = (heroID) => { // Allow for hero_name to be passed in and converted to heroID
    return `${ASSETS_URL.replace("eu.", "")}/${ASSETS_ENDPOINTS.heroes}/${heroID}/hero_face.png`
}

const getItemAssetURL = (itemName) => {
    return `${ASSETS_URL.replace("eu.", "")}/${ASSETS_ENDPOINTS.items}/${itemName}.png`
}


const response_type_replay_buffer = { responseType: "arraybuffer" }

const getHeroesNames = async () => {
    const response = await axios.get(`${API_URL}/${API_ENDPOINTS.heroes}`, response_type_replay_buffer)
    const decoded = decode(Buffer.from(response.data))
    return decoded
}


const getItems = async () => {
    const response = await axios.get(`${API_URL}/${API_ENDPOINTS.items}`, response_type_replay_buffer)
    const decoded = decode(Buffer.from(response.data))
    return decoded
}

const getPlayer = async (player_ID_or_name) => {
    const response = await axios.get(`${API_URL}/${API_ENDPOINTS.player}?name=${player_ID_or_name}`, response_type_replay_buffer)
    const decoded = decode(Buffer.from(response.data))
    return decoded
}

const getMatch = async (matchID) => {
    const response = await axios.get(`${API_URL}/${API_ENDPOINTS.match}/${matchID}`, response_type_replay_buffer)
    const decoded = decode(Buffer.from(response.data))
    return decoded
}

const getMatches = async (numberOfMatches, additions=[], playerID=null) => {
    const getQueryParams = (playerID && `player=${playerID}` || "") + `&take=${numberOfMatches}`
    const response = await axios.get(`${API_URL}/${API_ENDPOINTS.matches}?${getQueryParams}&additions=${additions.join(",")}`, response_type_replay_buffer)
    const decoded = decode(Buffer.from(response.data))
    return decoded
}

const getLeaderboard = async (heroStats=true) => {
    heroStats = heroStats && 1 || 0
    const response = await axios.get(`${API_URL}/${API_ENDPOINTS.leaderboard}?herostats=${heroStats}`, response_type_replay_buffer)
    const decoded = decode(Buffer.from(response.data))
    return decoded
}

export default {
    getHeroAssetURL,
    getItemAssetURL,

    getHeroesNames,
    getItems,
    getPlayer,
    getMatch,
    getMatches,
    getLeaderboard,
}
