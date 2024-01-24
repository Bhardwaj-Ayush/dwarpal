import Box from "./box";
import Dwarpal from "./dwarpal";

export default function main(params) {
    return (<>
        <Dwarpal />
        <div className="grid grid-cols-2 gap-4 md:grid-cols-3 w-full my-8">
            <Box text="Check whether Terms and Conditions Stated on a website are good for you or not and summarizes"  title="Dwarpal"/>
            <Box text="Check for Harmful Pattern on given site" title="Security"/>
            <Box text="Check if for Other Other Securty Checks" title="Privacy"/>
            <Box text="Check for Harmful Pattern on given site" title="Features"/>
            <Box text="Check if for Other Other Securty Checks" title="Paraphrase TnC" />            
        </div>

    </>)
}

