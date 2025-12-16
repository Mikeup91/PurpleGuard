import React, { useEffect, useState } from 'react';

// Assuming your SoundEngine is in a separate file
// If it's not created yet, we can create it next
const triggerBreachAlarm = () => {
    const audioCtx = new (window.AudioContext || (window as any).webkitAudioContext)();
    const oscillator = audioCtx.createOscillator();
    oscillator.type = 'sawtooth';
    oscillator.frequency.setValueAtTime(440, audioCtx.currentTime);
    oscillator.connect(audioCtx.destination);
    oscillator.start();
    oscillator.stop(audioCtx.currentTime + 0.1);
};

const PurpleGuardDashboard = () => {
    const [metadata, setMetadata] = useState({ total_kills: 0, findings: [] });
    const [lastKillCount, setLastKillCount] = useState(0);

    useEffect(() => {
        const fetchStats = async () => {
            try {
                const response = await fetch('/metadata.json');
                const data = await response.json();
                setMetadata(data);

                if (data.total_kills > lastKillCount) {
                    triggerBreachAlarm(); 
                    setLastKillCount(data.total_kills);
                }
            } catch (err) {
                console.error("Link to Omnibus Engine broken:", err);
            }
        };

        const interval = setInterval(fetchStats, 3000);
        return () => clearInterval(interval);
    }, [lastKillCount]);

    return (
        <div className="p-8 bg-black text-green-500 font-mono min-h-screen">
            <h1 className="text-3xl mb-4 text-red-600 font-bold">PURPLEGUARD v3.2 LIVE FEED</h1>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="border border-red-900 p-4 bg-gray-900">
                    <h2 className="text-xl">Breach Rate: 100%</h2>
                    <p className="text-6xl font-bold text-red-500">{metadata.total_kills}</p>
                    <p className="text-gray-400">CONFIRMED KILLS</p>
                </div>
                <div className="border border-green-900 p-4 bg-gray-900 overflow-y-auto h-96">
                    <h2 className="text-xl mb-4 text-white border-b border-green-900">Live Kill Feed</h2>
                    {metadata.findings && [...metadata.findings].reverse().slice(0, 20).map((v: any, i: number) => (
                        <div key={i} className="text-xs border-b border-gray-800 py-2">
                            <span className="text-red-500 font-bold">[BREACH]</span> {v.type} <br/>
                            <span className="text-gray-500 text-[10px]">{v.target}</span>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default PurpleGuardDashboard;
